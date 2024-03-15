import ee
import folium


def add_ee_layer(
    map_widget: folium.Map, ee_image_object: ee.Image, vis_params: dict, name: str
) -> None:
    """
    Adds a Google Earth Engine image layer to a Folium map.

    Args:
        map_widget (folium.Map): Folium map object to which the layer is added.
        ee_image_object (ee.Image): Google Earth Engine image object.
        vis_params (dict): Visualization parameters for the image.
        name (str): Name of the layer to display on the map.

    Returns:
        None
    """
    # Get the map ID for the Google Earth Engine image
    map_id_dict = ee.Image(ee_image_object).getMapId(vis_params)

    # Create a Folium map layer using the map ID
    tile_layer = folium.raster_layers.TileLayer(
        tiles=map_id_dict["tile_fetcher"].url_format,
        attr='Map Data &copy; <a href="https://earthengine.google.com/">Google Earth Engine</a>',
        name=name,
        overlay=True,
        control=True,
    )

    # Add the layer to the Folium map
    tile_layer.add_to(map_widget)
