import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER


def mpl_params(size=12, font_family='Candara', mathtext = 'stixsans', title_size = 14):
    """ 
    plt.rcParams.update(my_params(size=16, font_family='Candara'))

    https://jonathansoma.com/lede/data-studio/matplotlib/list-all-fonts-available-in-matplotlib-plus-samples/
    """
    plt.style.use('default')
    params = {'legend.fontsize': size, 
            'xtick.labelsize':size, 
            'ytick.labelsize':size, 
            'font.size':size,
            'font.family':font_family,
            'mathtext.fontset': mathtext,
            'mathtext.bf':'STIXGeneral:bold',
            'axes.titlesize': title_size,
            'figure.titlesize': title_size,
            'figure.dpi': 200,
            'figure.facecolor': 'white',}

    return params

def map_params(projection_str='PlateCarree', figsize=(10, 8), extent='global', gl_and_labels=True):
    projection_dict = {
                'PlateCarree': ccrs.PlateCarree(),
                'Mercator': ccrs.Mercator(),
                'Robinson': ccrs.Robinson(),
                'Mollweide': ccrs.Mollweide(),
                'Orthographic': ccrs.Orthographic(),
                }
    fig,ax = plt.subplots(subplot_kw={'projection': projection_dict[projection_str]}, figsize=figsize)
#     ax = plt.axes(projection=projection_dict[projection_str], figsize=figsize)
    if extent == 'global':
        ax.set_global()
    else:
        ax.set_extent(extent, crs=ccrs.PlateCarree())

    # Add land
    land = cfeature.NaturalEarthFeature('physical', 'land', '50m',
                                        edgecolor='face', facecolor='lightgray')
    ax.add_feature(land, zorder=0)

    if gl_and_labels:
        gl = ax.gridlines(draw_labels=True, linewidth=1, color='gray', alpha=0.25, linestyle='--')
        gl.xlabels_top = False
        gl.ylabels_right = False
        gl.xformatter = LONGITUDE_FORMATTER
        gl.yformatter = LATITUDE_FORMATTER
        gl.xlabel_style = {'size': 10, 'color': 'black'}
        gl.ylabel_style = {'size': 10, 'color': 'black'}

    return ax

