try:
    from mpl_toolkits.basemap import Basemap
    import matplotlib.pyplot as plt
    
    # Simple coastlines map
    fig = plt.figure(figsize=(12, 12))
    m = Basemap()
    m.drawcoastlines(linewidth=1.0, linestyle='dashed', color='red')
    plt.title("Coastlines", fontsize=20)
    plt.show()
    
    # Map with a marker
    fig = plt.figure(figsize=(8, 8))
    m = Basemap(projection='lcc',
                resolution=None,
                width=8E6, height=8E6,
                lat_0=45, lon_0=-100,)
    m.etopo(scale=0.5, alpha=0.5)
    
    # Map (long, lat) to (x, y) for plotting
    x, y = m(-122.3, 47.6)
    plt.plot(x, y, 'ok', markersize=5)
    plt.text(x, y, ' Seattle', fontsize=12)
    plt.show()
    
except ImportError:
    print("Basemap is not installed. You need to install it using 'conda install basemap'")
    
    # Alternative using geopandas if available
    try:
        import geopandas as gpd
        
        # Try to use world dataset that comes with geopandas
        world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
        
        # Plot countries
        world.plot()
        plt.title("World Map using GeoPandas")
        plt.show()
    except ImportError:
        print("GeoPandas is also not installed.")