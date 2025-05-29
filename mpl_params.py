def my_params(size=12, font_family='Futura', title_size = 14):
    """ 
    Use: plt.rcParams.update(crplot.my_params(size=16))
    """
    plt.style.use('default')
    params = {'legend.fontsize': size, 
            'xtick.labelsize':size, 
            'ytick.labelsize':size, 
            'font.size':size,
            'font.family':font_family,
            'mathtext.fontset':'stixsans',
            'mathtext.bf':'STIXGeneral:bold',
            'axes.titlesize': title_size,
            'figure.titlesize': title_size,}
    return params
