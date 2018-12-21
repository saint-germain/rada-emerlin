import numpy as np
import sys
import collections
import itertools

obsMERLIN = {'m0': {'unit': 'rad', 'value': -0.0402909257822891 },
 'm1': {'unit': 'rad', 'value':  0.9291556978964651},
 'm2': {'unit': 'm', 'value': 0.0},
 'refer': 'WGS84',
 'type': 'position'}

def get_field_names(msfile):
    tb.open(msfile+'/FIELD')
    field_names = tb.getcol('NAME')
    tb.close()
    return field_names

def get_innerchan(msfile, frac=0.9):
    ms.open(msfile)
    axis_info = ms.getdata(['axis_info'], ifraxis=True)
    ms.close()
    nchan = len(axis_info['axis_info']['freq_axis']['chan_freq'][:,0])
    bchan = (1-frac)*(nchan-nchan/512.)
    echan = frac*(nchan-nchan/512.)
    innerchan = '{0:.0f}~{1:.0f}'.format(bchan, echan)
    return innerchan, int(bchan), int(echan)

def get_msprop(msfile):
    ms.open(msfile)
    axis_info = ms.getdata(['axis_info', 'scan_number', 'field_id', 'time'],ifraxis=True)
    ms.close()
    return axis_info

def check_band(msfile):
    # Take first frequency in the MS
    ms.open(msfile)
    freq = ms.getdata(['axis_info'])['axis_info']['freq_axis']['chan_freq'][0][0]/1e9
    ms.close()
    band = '' 
    if (freq > 1.2) and (freq < 1.7):
        band = 'L'
    if (freq > 4) and (freq < 8):
        band = 'C'
    if (freq > 22) and (freq < 24): 
        band = 'K'
    return band 


def get_phase_center(msfile, field_id):
    vhead = vishead(msfile, mode = 'list', listitems = 'ptcs')
    ra_float = vhead['ptcs'][0]['r'+str(field_id+1)][0][0][0]*180./np.pi/15. + 24.
    de_float = vhead['ptcs'][0]['r'+str(field_id+1)][1][0][0]*180./np.pi
    # RA
    ra_h = int(ra_float)
    ra_min_m = (ra_float-ra_h)*60.0
    ra_m = int(ra_min_m)
    ra_s = (ra_min_m-ra_m)*60.0
    ra = (ra_h,ra_m,ra_s)
    # Dec
    if np.sign(de_float)==-1: signo = '-'
    if np.sign(de_float)== 1: signo = '+'
    de_d = int(de_float)
    de_min_m = (abs(de_float-de_d))*60.0
    de_m = int(de_min_m)
    de_s = (de_min_m-de_m)*60.0
    de = (de_d,de_m,de_s)
    srcCoord = 'J2000 {0:02.0f}h{1:02.0f}m{2:06.3f}s {3:02.0f}d{4:02.0f}m{5:08.5f}s'.format(ra_h,ra_m,ra_s, de_d,de_m,de_s)
    return ra, de, srcCoord

def calc_azel(tm, srcCoord = ''):
    az = np.zeros(len(tm))
    el = np.zeros(len(tm))
    me.doframe(obsMERLIN)
    (ep,ra,dec) = srcCoord.split(" ")[0:3]
    b = me.direction(ep,qa.toangle(ra),dec)
    for i in range(len(tm)):
        a = me.epoch('utc', qa.quantity(tm[i],'d'))
        me.measure(a, 'tai') # convert to IAT  
        me.doframe(a) # set time in frame  
        azi = me.getvalue(me.measure(b,'azel'))['m0']['value']*180.0/np.pi
        eli = me.getvalue(me.measure(b,'azel'))['m1']['value']*180.0/np.pi
        az[i] = azi
        el[i] = eli
    return az, el

def get_fields_coords(msfile):
    ms.open(msfile)
    axis_info = ms.getdata(['field_id'],ifraxis=True)
    ms.close()
    field_ids = np.unique(axis_info['field_id'])
    srcCoords = {}
    for field_id in field_ids:
        srcCoords[field_id] = get_phase_center(msfile, field_id)[2]
    return srcCoords

def calc_azel(tm, srcCoord = ''):
    az = np.zeros(len(tm))
    el = np.zeros(len(tm))
    me.doframe(obsMERLIN)
    (ep,ra,dec) = srcCoord.split(" ")[0:3]
    b = me.direction(ep,qa.toangle(ra),dec)
    for i in range(len(tm)):
        a = me.epoch('utc', qa.quantity(tm[i],'d'))
        me.measure(a, 'tai') # convert to IAT  
        me.doframe(a) # set time in frame  
        azi = me.getvalue(me.measure(b,'azel'))['m0']['value']*180.0/np.pi
        eli = me.getvalue(me.measure(b,'azel'))['m1']['value']*180.0/np.pi
        az[i] = azi
        el[i] = eli
    return az, el


def select_pol(pol):
    """ Select only unflagged visibilities from the relevant correlations. 
    The output is a 1D array, because unflagged data are selected independently
    from each polarization """
    if pol.upper() == 'HALF' or pol.upper() == 'RR,LL':
        pol_n = np.r_[0, 3]
    elif pol.upper() == 'RR':
        pol_n = np.r_[0]
    elif pol.upper() == 'LL':
        pol_n = np.r_[3]
    elif pol.upper() == 'RL':
        pol_n = np.r_[1]
    elif pol.upper() == 'LR':
        pol_n = np.r_[2]
    elif pol.upper() == 'ALL' or pol == '':
        pol_n = np.r_[0,1,2,3]
    return pol_n

def get_msinfo(msfile):
    axis_info = get_msprop(msfile)
    field_names = get_field_names(msfile)
    #antennas = read_antennas(msfile)

    num_spw = len(vishead(msfile, mode = 'list', listitems = ['spw_name'])['spw_name'][0])
    #baselines = get_baselines(msfile)
    #innerchan = get_innerchan(msfile, frac=0.8)[0]

    field_ids = axis_info['field_id']
    scan_numbers = axis_info['scan_number']
    all_scans = np.unique(axis_info['scan_number'])

    #resolutions = np.mean(axis_info['axis_info']['freq_axis']['resolution'], axis=0)
    #frequencies = np.mean(axis_info['axis_info']['freq_axis']['chan_freq'], axis=0)

    #srcCoords = get_fields_coords(msfile)
    info = {}
    #info['baselines'] = baselines
    info['num_spw'] = num_spw
    info['field_names'] = field_names
    info['field_ids'] = field_ids
    #info['time'] = axis_info['time']
    #info['innerchan'] = innerchan
    info['all_scans'] = all_scans
    info['scan_numbers'] = scan_numbers
    #info['resolutions'] = resolutions
    #info['frequencies'] = frequencies
    #info['srcCoords'] = srcCoords
    band = check_band(msfile)
    info['band'] = band
    return info


def select_data(msfile, spw, scan=None, field=None, bsl=None):
    if scan is not None:
        scan = str(scan)
    ms.open(msfile)
    staql={'spw': str(spw), 'field':field, 'baseline':bsl, 'scan':scan}
    ms.msselect(staql)
    d = ms.getdata(['model_real', 'residual_real', 'corrected_real', 'flag', 'axis_info'], ifraxis=True)
    ms.close()
    corrected_real = d['corrected_real']
    residual_real = d['residual_real']
    return corrected_real, residual_real, d['flag'], d['axis_info']

def find_slices(bchan=None, echan=None, bsl='', pol='RR,LL'):
    slice_pol = select_pol(pol)
    slice_chan = slice(bchan, echan)
    if bsl == None or bsl == '':
        slice_bsl = slice(None, None)
    else:
        slice_bsl = slice(bsl, bsl+1)
    return slice_pol, slice_chan, slice_bsl

def get_spw(msfile, scan=''):
    ms.open(msfile)
    staql={'scan':str(scan)}
    ms.msselect(staql)
    d = ms.getdata(['data_desc_id'], ifraxis=True)
    ms.close()
    return np.unique(d['data_desc_id'])

def process_data(msfile, scan, info, bchan, echan, pol, fields, band):
    rows = np.where(info['scan_numbers'] == int(scan))
    field_id = np.unique(info['field_ids'][rows])[0]
    field_name = info['field_names'][field_id]
    field_info = {'field_id':field_id, 'field_name':field_name}
    slice_pol, slice_chan, slice_bsl = find_slices(bchan=bchan,
                                                   echan=echan,
                                                   bsl=None,
                                                   pol=pol)
    if field_name in fields.replace(' ', '').split(',') or fields == '':
        print field_name
        for spw in get_spw(msfile, scan=scan):
            #print ('spw: {}'.format(spw))
            calc_stats(msfile, spw, scan,
                       slice_pol, slice_chan, slice_bsl, field_info, band)



def get_rms(rms, baselines, a1,a2):
    value = np.nan
    try:
        value = rms[baselines == '{0}-{1}'.format(a1,a2)][0]
    except:
        pass
    try:
        value = rms[baselines == '{0}-{1}'.format(a2,a1)][0]
    except:
        pass
    return value

def rms2sefd(rms, channel_width, int_time, baselines, band):
    if band == 'L':
        kappa = 1.633 # improvement in SNR due to Hanning smoothing. kappa=1.633 for 3 chan hanning
    else:
        kappa = 1
    antennas = list(collections.OrderedDict.fromkeys(','.join(baselines).replace('-',',').split(',')))
    baselines = np.array(baselines)
    nu = 0.93  # WIDAR correlator efficiency (estimate from VLA)
    beta = channel_width
    tau = int_time
    s0 = 0 # We are using std, and when possible residuals with the model subtracted
    sefdij = np.sqrt(rms**2-s0**2)*np.sqrt(2)*nu*kappa*np.sqrt(tau*beta)

    sefd = {}
    for ant1 in antennas:
        ant_reduced = list(antennas)
        ant_reduced.remove(ant1)
        bslist = []
        bslist.extend(itertools.combinations(ant_reduced, 2))
        sefdi = []
        for bsl in bslist:
            bsl1 = get_rms(sefdij, baselines, ant1, bsl[0])
            bsl2 = get_rms(sefdij, baselines, ant1, bsl[1])
            bsl3 = get_rms(sefdij, baselines, bsl[0], bsl[1])
            nargh = bsl1*bsl2/bsl3
            sefdi.append(nargh)
        sefd[ant1] = np.nanmean(sefdi)
    return sefd


def calc_stats(msfile, spw, scan, slice_pol, slice_chan, slice_bsl, field_info, band):
    global res, first_line, srcCoords
    data = select_data(msfile, spw=spw, scan=scan)
    corrected_real, residual_real, flag, axis_info = data
    r_corrected = corrected_real[slice_pol, slice_chan, slice_bsl]
    r_residual  = residual_real[slice_pol, slice_chan, slice_bsl]
    f = ~flag[slice_pol, slice_chan, slice_bsl]
    r_corrected[~f] = np.nan
    r_residual[~f] = np.nan
    r_corrected_mean = np.nanmean(r_corrected, axis=(0,1,3))
    r_corrected_std  = np.nanstd(r_corrected, axis=(0,1,3))
    r_residual_mean = np.nanmean(r_residual, axis=(0,1,3))
    r_residual_std  = np.nanstd(r_residual, axis=(0,1,3))
    baselines = axis_info['ifr_axis']['ifr_name'][slice_bsl]

    polarizations = axis_info['corr_axis'][slice_pol]
    chan_frequency = axis_info['freq_axis']['chan_freq'][slice_chan]
    channel_width = np.mean(axis_info['freq_axis']['resolution'][slice_chan])
    time_mjd = axis_info['time_axis']['MJDseconds']/60./60./24.
    time_scan_mjd = np.mean(time_mjd)
    az, el = calc_azel([time_scan_mjd], srcCoord=srcCoords[field_info['field_id']])
    int_time = np.median(np.diff(axis_info['time_axis']['MJDseconds']))
    sefd = rms2sefd(r_residual_std, channel_width, int_time, baselines, band)
#    ant1, ant2 = baseline.split('-')
    result = collections.OrderedDict()
    result['scan'] = scan
    result['field_name'] = field_info['field_name']
    result['field_id'] = field_info['field_id']
#    result['baseline'] = baseline
#    result['ant1'] = ant1
#    result['ant2'] = ant2
    result['polarizations'] = '-'.join(polarizations)
    result['spw'] = spw
    result['freq'] = np.mean(chan_frequency)
    result['freq_ini'] = np.min(chan_frequency)
    result['freq_end'] = np.max(chan_frequency)
    result['channel_width'] = channel_width
    result['int_time'] = int_time
    result['time_mjd'] = time_scan_mjd
    result['time_mjd_ini'] = np.min(time_mjd)
    result['time_mjd_end'] = np.max(time_mjd)
    result['az'] = az[0]
    result['el'] = el[0]
    result['r_corrected_mean'] = np.mean(r_corrected_mean)
    result['r_corrected_std'] = np.mean(r_corrected_std)
    result['r_residual_mean'] = np.mean(r_residual_mean)
    result['r_residual_std'] = np.mean(r_residual_std)
    for ant1 in sefd.keys():
        result['antenna'] = ant1
        result['sefd'] = sefd[ant1]
        if first_line == False:
            res.write(','.join([str(item) for item in result.keys()]))
            res.write('\n')
            first_line = True
        res.write(','.join([str(item) for item in result.values()]))
        res.write('\n')
    res.flush()


def main(msfile, fields):
    global res, first_line, srcCoords
    pol = 'RR,LL'
    innerchan, bchan, echan = get_innerchan(msfile, frac=0.8)
    fields = ''
    srcCoords = get_fields_coords(msfile)
    info = get_msinfo(msfile)
    scans = info['all_scans']
    band = info['band']
    first_line = False
    res = open('results.csv', 'wb')
    for scan in scans:
        print('{0:3}/{1}'.format(scan,np.max(scans)))
        results = process_data(msfile=msfile, scan=scan,
                               info=info, fields=fields,
                               bchan=bchan, echan=echan,
                               pol=pol, band=band)
    res.close()

if __name__ == '__main__':
    msfile = sys.argv[-1]
    fields = ''
    main(msfile, fields)



