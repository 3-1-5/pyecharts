import simplejson as json

from ..globals import BMapType
from .global_options import TooltipOpts
from .series_options import (
    BasicOpts,
    ItemStyleOpts,
    JSFunc,
    LabelOpts,
    LineStyleOpts,
    Numeric,
    Optional,
    Sequence,
    TextStyleOpts,
    Union,
)


class SunburstItem(BasicOpts):
    def __init__(
        self,
        value: Optional[Numeric] = None,
        name: Optional[str] = None,
        link: Optional[str] = None,
        target: Optional[str] = "blank",
        label_opts: Union[LabelOpts, dict, None] = None,
        itemstyle_opts: Union[ItemStyleOpts, dict, None] = None,
        children: Optional[Sequence] = None,
    ):
        self.opts: dict = {
            "value": value,
            "name": name,
            "link": link,
            "target": target,
            "label": label_opts,
            "itemStyle": itemstyle_opts,
            "children": children,
        }


class GraphNode(BasicOpts):
    def __init__(
        self,
        name: Optional[str] = None,
        x: Optional[Numeric] = None,
        y: Optional[Numeric] = None,
        is_fixed: bool = False,
        value: Union[str, Sequence, None] = None,
        category: Optional[int] = None,
        symbol: Optional[str] = None,
        symbol_size: Union[Numeric, Sequence, None] = None,
        label_opts: Union[LabelOpts, dict, None] = None,
    ):
        self.opts: dict = {
            "name": name,
            "x": x,
            "y": y,
            "fixed": is_fixed,
            "value": value,
            "category": category,
            "symbol": symbol,
            "symbolSize": symbol_size,
            "label": label_opts,
        }


class GraphLink(BasicOpts):
    def __init__(
        self,
        source: Union[str, int, None] = None,
        target: Union[str, int, None] = None,
        value: Optional[Numeric] = None,
        symbol: Union[str, Sequence, None] = None,
        symbol_size: Union[Numeric, Sequence, None] = None,
        linestyle_opts: Union[LineStyleOpts, dict, None] = None,
        label_opts: Union[LabelOpts, dict, None] = None,
    ):
        self.opts: dict = {
            "source": source,
            "target": target,
            "value": value,
            "symbol": symbol,
            "symbolSize": symbol_size,
            "lineStyle": linestyle_opts,
            "label": label_opts,
        }


class GraphCategory(BasicOpts):
    def __init__(
        self,
        name: Optional[str] = None,
        symbol: Optional[str] = None,
        symbol_size: Union[Numeric, Sequence, None] = None,
        label_opts: Union[LabelOpts, dict, None] = None,
    ):
        self.opts: dict = {
            "name": name,
            "symbol": symbol,
            "symbolSize": symbol_size,
            "label": label_opts,
        }


class TreeItem(BasicOpts):
    def __init__(
        self,
        name: Optional[str] = None,
        value: Optional[Numeric] = None,
        label_opts: Union[LabelOpts, dict, None] = None,
        children: Optional[Sequence] = None,
    ):
        self.opts: dict = {
            "name": name,
            "value": value,
            "children": children,
            "label": label_opts,
        }


class BMapNavigationControlOpts(BasicOpts):
    def __init__(
        self,
        position: Numeric = BMapType.ANCHOR_TOP_LEFT,
        offset_width: Numeric = 10,
        offset_height: Numeric = 10,
        type_: Numeric = BMapType.NAVIGATION_CONTROL_LARGE,
        is_show_zoom_info: bool = False,
        is_enable_geo_location: bool = False,
    ):
        bmap_nav_config = json.dumps(
            {
                "anchor": position,
                "offset": {"width": offset_width, "height": offset_height},
                "type": type_,
                "showZoomInfo": is_show_zoom_info,
                "enableGeolocation": is_enable_geo_location,
            }
        )

        self.opts: dict = {
            "functions": [
                "bmap.addControl(new BMap.NavigationControl({}));".format(
                    bmap_nav_config
                )
            ]
        }


class BMapOverviewMapControlOpts(BasicOpts):
    def __init__(
        self,
        position: Numeric = BMapType.ANCHOR_BOTTOM_RIGHT,
        offset_width: Numeric = 10,
        offset_height: Numeric = 50,
        is_open: bool = False,
    ):
        bmap_overview_config = json.dumps(
            {
                "anchor": position,
                "offset": {"width": offset_width, "height": offset_height},
                "isOpen": is_open,
            }
        )

        self.opts: dict = {
            "functions": [
                "var overview = new BMap.OverviewMapControl({});".format(
                    bmap_overview_config
                ),
                "bmap.addControl(overview);",
            ]
        }


class BMapScaleControlOpts(BasicOpts):
    def __init__(
        self,
        position: Numeric = BMapType.ANCHOR_BOTTOM_LEFT,
        offset_width: Numeric = 80,
        offset_height: Numeric = 21,
    ):
        bmap_scale_config = json.dumps(
            {
                "anchor": position,
                "offset": {"width": offset_width, "height": offset_height},
            }
        )

        self.opts: dict = {
            "functions": [
                "bmap.addControl(new BMap.ScaleControl({}));".format(bmap_scale_config)
            ]
        }


class BMapTypeControlOpts(BasicOpts):
    def __init__(
        self,
        position: Numeric = BMapType.ANCHOR_TOP_RIGHT,
        type_: Numeric = BMapType.MAPTYPE_CONTROL_HORIZONTAL,
    ):
        bmap_type_config = json.dumps({"anchor": position, "type": type_})

        self.opts: dict = {
            "functions": [
                "bmap.addControl(new BMap.MapTypeControl({}));".format(bmap_type_config)
            ]
        }


class BMapCopyrightTypeOpts(BasicOpts):
    def __init__(
        self,
        position: Numeric = BMapType.ANCHOR_BOTTOM_LEFT,
        offset_width: Numeric = 2,
        offset_height: Numeric = 2,
        copyright_: str = "",
    ):
        bmap_copyright_config = json.dumps(
            {
                "anchor": position,
                "offset": {"width": offset_width, "height": offset_height},
            }
        )

        bmap_copyright_content_config = json.dumps({"id": 1, "content": copyright_})

        self.opts: dict = {
            "functions": [
                "var copyright = new BMap.CopyrightControl({});".format(
                    bmap_copyright_config
                ),
                "copyright.addCopyright({});".format(bmap_copyright_content_config),
                "bmap.addControl(copyright);",
            ]
        }


class BMapGeoLocationControlOpts(BasicOpts):
    def __init__(
        self,
        position: Numeric = BMapType.ANCHOR_BOTTOM_LEFT,
        offset_width: Numeric = 10,
        offset_height: Numeric = 10,
        is_show_address_bar: bool = True,
        is_enable_auto_location: bool = False,
    ):
        bmap_geo_location_config = json.dumps(
            {
                "anchor": position,
                "offset": {"width": offset_width, "height": offset_height},
                "showAddressBar": is_show_address_bar,
                "enableAutoLocation": is_enable_auto_location,
            }
        )

        self.opts: dict = {
            "functions": [
                "bmap.addControl(new BMap.GeolocationControl({}))".format(
                    bmap_geo_location_config
                )
            ]
        }


class BarItem(BasicOpts):
    def __init__(
        self,
        name: Optional[str] = None,
        value: Optional[Numeric] = None,
        label_opts: Union[LabelOpts, dict, None] = None,
        itemstyle_opts: Union[ItemStyleOpts, dict, None] = None,
        tooltip_opts: Union[TooltipOpts, dict, None] = None,
    ):
        self.opts: dict = {
            "name": name,
            "value": value,
            "label": label_opts,
            "itemStyle": itemstyle_opts,
            "tooltip": tooltip_opts,
        }


class ComponentTitleOpts:
    def __init__(
        self,
        title: str = "",
        subtitle: str = "",
        title_style: Optional[dict] = None,
        subtitle_style: Optional[dict] = None,
    ):
        self.title = title.replace("\n", "<br/>")
        self.subtitle = subtitle.replace("\n", "<br/>")
        self.title_style: str = ""
        self.subtitle_style: str = ""
        title_style = title_style or {"style": "font-size: 18px; font-weight:bold;"}
        subtitle_style = subtitle_style or {"style": "font-size: 12px;"}
        self._convert_dict_to_string(title_style, subtitle_style)

    def _convert_dict_to_string(self, title_style: dict, subtitle_style: dict):
        for k, v in title_style.items():
            self.title_style += '{}="{}" '.format(k, v)
        for k, v in subtitle_style.items():
            self.subtitle_style += '{}="{}" '.format(k, v)


class PageLayoutOpts(BasicOpts):
    def __init__(
        self,
        justify_content: Optional[str] = None,
        margin: Optional[str] = None,
        display: Optional[str] = None,
        flex_wrap: Optional[str] = None,
    ):
        self.opts: dict = {
            "justify-content": justify_content,
            "margin": margin,
            "display": display,
            "flex-wrap": flex_wrap,
        }


class BaseGraphic(BasicOpts):
    pass


class GraphicShapeOpts(BaseGraphic):
    def __init__(
        self,
        pos_x: Numeric = 0,
        pos_y: Numeric = 0,
        width: Numeric = 0,
        height: Numeric = 0,
        r: Union[Sequence, Numeric, None] = None,
    ):
        self.opts: dict = {
            "x": pos_x,
            "y": pos_y,
            "width": width,
            "height": height,
            "r": r,
        }


class GraphicBasicStyleOpts(BaseGraphic):
    def __init__(
        self,
        fill: str = "#000",
        stroke: Optional[str] = None,
        line_width: Numeric = 0,
        shadow_blur: Optional[Numeric] = None,
        shadow_offset_x: Optional[Numeric] = None,
        shadow_offset_y: Optional[Numeric] = None,
        shadow_color: Optional[str] = None,
    ):
        self.opts: dict = {
            "fill": fill,
            "stroke": stroke,
            "line_width": line_width,
            "shadowBlur": shadow_blur,
            "shadowOffsetX": shadow_offset_x,
            "shadowOffsetY": shadow_offset_y,
            "shadowColor": shadow_color,
        }


class GraphicImageStyleOpts(BaseGraphic):
    def __init__(
        self,
        image: Optional[str] = None,
        pos_x: Numeric = 0,
        pos_y: Numeric = 0,
        width: Numeric = 0,
        height: Numeric = 0,
        opacity: Numeric = 1,
        graphic_basicstyle_opts: Union[GraphicBasicStyleOpts, dict, None] = None,
    ):
        self.opts: dict = {
            "image": image,
            "x": pos_x,
            "y": pos_y,
            "width": width,
            "height": height,
            "opacity": opacity,
        }

        if graphic_basicstyle_opts:
            if isinstance(graphic_basicstyle_opts, GraphicBasicStyleOpts):
                self.opts.update(graphic_basicstyle_opts.opts)
            else:
                self.opts.update(graphic_basicstyle_opts)


class GraphicTextStyleOpts(BaseGraphic):
    def __init__(
        self,
        text: Optional[JSFunc] = None,
        pos_x: Numeric = 0,
        pos_y: Numeric = 0,
        font: Optional[str] = None,
        text_align: str = "left",
        text_vertical_align: Optional[str] = None,
        graphic_basicstyle_opts: Union[GraphicBasicStyleOpts, dict, None] = None,
    ):
        self.opts: dict = {
            "text": text,
            "x": pos_x,
            "y": pos_y,
            "font": font,
            "textAlign": text_align,
            "textVerticalAlign": text_vertical_align,
        }

        if graphic_basicstyle_opts:
            if isinstance(graphic_basicstyle_opts, GraphicBasicStyleOpts):
                self.opts.update(graphic_basicstyle_opts.opts)
            else:
                self.opts.update(graphic_basicstyle_opts)


class GraphicItem(BaseGraphic):
    def __init__(
        self,
        id_: Optional[str] = None,
        action: str = "merge",
        position: [Sequence, Numeric, None] = None,
        rotation: Union[Numeric, JSFunc, None] = 0,
        scale: Union[Sequence, Numeric, None] = None,
        origin: Union[Numeric, Sequence, None] = None,
        left: Union[Numeric, str, None] = None,
        right: Union[Numeric, str, None] = None,
        top: Union[Numeric, str, None] = None,
        bottom: Union[Numeric, str, None] = None,
        bounding: str = "all",
        z: Numeric = 0,
        z_level: Numeric = 0,
        is_silent: bool = False,
        is_invisible: bool = False,
        is_ignore: bool = False,
        cursor: str = "pointer",
        is_draggable: bool = False,
        is_progressive: bool = False,
        width: Numeric = 0,
        height: Numeric = 0,
    ):
        self.opts: dict = {
            "id": id_,
            "$action": action,
            "position": position,
            "rotation": rotation,
            "scale": scale,
            "origin": origin,
            "left": left,
            "right": right,
            "top": top,
            "bottom": bottom,
            "bounding": bounding,
            "z": z,
            "zlevel": z_level,
            "silent": is_silent,
            "invisible": is_invisible,
            "ignore": is_ignore,
            "cursor": cursor,
            "draggable": is_draggable,
            "progressive": is_progressive,
            "width": width,
            "height": height,
        }


class GraphicGroup(BaseGraphic):
    def __init__(
        self,
        graphic_item: Union[GraphicItem, dict, None] = None,
        is_diff_children_by_name: bool = False,
        children: Optional[Sequence[BaseGraphic]] = None,
    ):
        self.opts: dict = {
            "type": "group",
            "diffChildrenByName": is_diff_children_by_name,
            "children": children,
        }

        if graphic_item:
            if isinstance(graphic_item, GraphicItem):
                self.opts.update(graphic_item.opts)
            else:
                self.opts.update(graphic_item)


class GraphicImage(BaseGraphic):
    def __init__(
        self,
        graphic_item: Union[GraphicItem, dict, None] = None,
        graphic_imagestyle_opts: Union[GraphicImageStyleOpts, dict, None] = None,
    ):
        self.opts: dict = {"type": "image"}

        if graphic_item:
            if isinstance(graphic_item, GraphicItem):
                self.opts.update(graphic_item.opts)
            else:
                self.opts.update(graphic_item)

        if graphic_imagestyle_opts:
            if isinstance(graphic_imagestyle_opts, GraphicImageStyleOpts):
                self.opts.update(style=graphic_imagestyle_opts.opts)
            else:
                self.opts.update(style=graphic_imagestyle_opts)


class GraphicText(BaseGraphic):
    def __init__(
        self,
        graphic_item: Union[GraphicItem, dict, None] = None,
        graphic_textstyle_opts: Union[GraphicTextStyleOpts, dict, None] = None,
    ):
        self.opts: dict = {"type": "text"}

        if graphic_item:
            if isinstance(graphic_item, GraphicItem):
                self.opts.update(graphic_item.opts)
            else:
                self.opts.update(graphic_item)

        if graphic_textstyle_opts:
            if isinstance(graphic_textstyle_opts, GraphicTextStyleOpts):
                self.opts.update(style=graphic_textstyle_opts.opts)
            else:
                self.opts.update(style=graphic_textstyle_opts)


class GraphicRect(BaseGraphic):
    def __init__(
        self,
        graphic_item: Union[GraphicItem, dict, None] = None,
        graphic_shape_opts: Union[GraphicShapeOpts, dict, None] = None,
        graphic_basicstyle_opts: Union[GraphicBasicStyleOpts, dict, None] = None,
    ):
        self.opts: dict = {"type": "rect"}

        if graphic_item:
            if isinstance(graphic_item, GraphicItem):
                self.opts.update(graphic_item.opts)
            else:
                self.opts.update(graphic_item)

        if graphic_shape_opts:
            if isinstance(graphic_shape_opts, GraphicShapeOpts):
                self.opts.update(shape=graphic_shape_opts.opts)
            else:
                self.opts.update(graphic_shape_opts)

        if graphic_basicstyle_opts:
            if isinstance(graphic_basicstyle_opts, GraphicBasicStyleOpts):
                self.opts.update(style=graphic_basicstyle_opts.opts)
            else:
                self.opts.update(style=graphic_basicstyle_opts)


class SankeyLevelsOpts(BasicOpts):
    def __init__(
        self,
        depth: Numeric = None,
        itemstyle_opts: Union[ItemStyleOpts, dict, None] = None,
        linestyle_opts: Union[LineStyleOpts, dict, None] = None,
    ):
        self.opts: dict = {
            "depth": depth,
            "itemStyle": itemstyle_opts,
            "lineStyle": linestyle_opts,
        }


class Map3DLabelOpts(BasicOpts):
    def __init__(
        self,
        is_show: bool = True,
        distance: Numeric = None,
        formatter: Optional[JSFunc] = None,
        text_style: Union[TextStyleOpts, dict, None] = None,
    ):
        self.opts: dict = {
            "show": is_show,
            "distance": distance,
            "formatter": formatter,
            "textStyle": text_style,
        }


class Map3DRealisticMaterialOpts(BasicOpts):
    def __init__(
        self,
        detail_texture: Optional[JSFunc] = None,
        texture_tiling: Numeric = 1,
        texture_offset: Numeric = 0,
        roughness: Numeric = 0.5,
        metalness: Numeric = 0,
        roughness_adjust: Numeric = 0.5,
        metalness_adjust: Numeric = 0.5,
        normal_texture: Optional[JSFunc] = None,
    ):
        self.opts: dict = {
            "detailTexture": detail_texture,
            "textureTiling": texture_tiling,
            "textureOffset": texture_offset,
            "roughness": roughness,
            "metalness": metalness,
            "roughnessAdjust": roughness_adjust,
            "metalnessAdjust": metalness_adjust,
            "normalTexture": normal_texture,
        }


class Map3DLambertMaterialOpts(BasicOpts):
    def __init__(
        self,
        detail_texture: Optional[JSFunc] = None,
        texture_tiling: Numeric = 1,
        texture_offset: Numeric = 0,
    ):
        self.opts: dict = {
            "detailTexture": detail_texture,
            "textureTiling": texture_tiling,
            "textureOffset": texture_offset,
        }


class Map3DColorMaterialOpts(BasicOpts):
    def __init__(
        self,
        detail_texture: Optional[JSFunc] = None,
        texture_tiling: Numeric = 1,
        texture_offset: Numeric = 0,
    ):
        self.opts: dict = {
            "detailTexture": detail_texture,
            "textureTiling": texture_tiling,
            "textureOffset": texture_offset,
        }


class Map3DLightOpts(BasicOpts):
    def __init__(
        self,
        main_color: str = "#fff",
        main_intensity: Numeric = 1,
        is_main_shadow: bool = False,
        main_shadow_quality: str = "medium",
        main_alpha: Numeric = 40,
        main_beta: Numeric = 40,
        ambient_color: str = "#fff",
        ambient_intensity: Numeric = 0.2,
        ambient_cubemap_texture: Optional[str] = None,
        ambient_cubemap_diffuse_intensity: Numeric = 0.5,
        ambient_cubemap_specular_intensity: Numeric = 0.5,
    ):
        self.opts: dict = {
            "main": {
                "color": main_color,
                "intensity": main_intensity,
                "shadow": is_main_shadow,
                "shadowQuality": main_shadow_quality,
                "alpha": main_alpha,
                "beta": main_beta,
            },
            "ambient": {"color": ambient_color, "intensity": ambient_intensity},
            "ambientCubemap": {
                "texture": ambient_cubemap_texture,
                "diffuseIntensity": ambient_cubemap_diffuse_intensity,
                "specularIntensity": ambient_cubemap_specular_intensity,
            },
        }


class Map3DPostEffectOpts(BasicOpts):
    def __init__(
        self,
        is_enable: bool = False,
        is_bloom_enable: bool = False,
        bloom_intensity: Numeric = 0.1,
        is_depth_field_enable: bool = False,
        depth_field_focal_distance: Numeric = 50,
        depth_field_focal_range: Numeric = 20,
        depth_field_fstop: Numeric = 2.8,
        depth_field_blur_radius: Numeric = 10,
        is_ssao_enable: bool = False,
        ssao_quality: str = "medium",
        ssao_radius: Numeric = 2,
        ssao_intensity: Numeric = 1,
        is_color_correction_enable: bool = False,
        color_correction_lookup_texture: Optional[JSFunc] = None,
        color_correction_exposure: Numeric = 0,
        color_correction_brightness: Numeric = 0,
        color_correction_contrast: Numeric = 1,
        color_correction_saturation: Numeric = 1,
        is_fxaa_enable: bool = False,
    ):
        self.opts: dict = {
            "enable": is_enable,
            "bloom": {"enable": is_bloom_enable, "bloomIntensity": bloom_intensity},
            "depthOfField": {
                "enable": is_depth_field_enable,
                "focalDistance": depth_field_focal_distance,
                "focalRange": depth_field_focal_range,
                "fstop": depth_field_fstop,
                "blurRadius": depth_field_blur_radius,
            },
            "SSAO": {
                "enable": is_ssao_enable,
                "quality": ssao_quality,
                "radius": ssao_radius,
                "intensity": ssao_intensity,
            },
            "colorCorrection": {
                "enable": is_color_correction_enable,
                "lookupTexture": color_correction_lookup_texture,
                "exposure": color_correction_exposure,
                "brightness": color_correction_brightness,
                "contrast": color_correction_contrast,
                "saturation": color_correction_saturation,
            },
            "FXAA": {"enable": is_fxaa_enable},
        }


class Map3DViewControlOpts(BasicOpts):
    def __init__(
        self,
        projection: str = "perspective",
        auto_rotate: bool = False,
        auto_rotate_direction: str = "cw",
        auto_rotate_speed: Numeric = 10,
        auto_rotate_after_still: Numeric = 3,
        damping: Numeric = 0.8,
        rotate_sensitivity: Union[Numeric, Sequence] = 1,
        zoom_sensitivity: Numeric = 1,
        pan_sensitivity: Numeric = 1,
        pan_mouse_button: str = "left",
        rotate_mouse_button: str = "middle",
        distance: Numeric = 100,
        min_distance: Numeric = 40,
        max_distance: Numeric = 400,
        orthographic_size: Numeric = 100,
        min_orthographic_size: Numeric = 20,
        max_orthographic_size: Numeric = 400,
        alpha: Numeric = 40,
        beta: Numeric = 0,
        center: Optional[Sequence] = None,
        min_alpha: Numeric = 5,
        max_alpha: Numeric = 90,
        min_beta: Numeric = -80,
        max_beta: Numeric = 80,
        animation: bool = True,
        animation_duration_update: Numeric = 1000,
        animation_easing_update: str = "cubicInOut",
    ):
        self.opts: dict = {
            "projection": projection,
            "autoRotate": auto_rotate,
            "autoRotateDirection": auto_rotate_direction,
            "autoRotateSpeed": auto_rotate_speed,
            "autoRotateAfterStill": auto_rotate_after_still,
            "damping": damping,
            "rotateSensitivity": rotate_sensitivity,
            "zoomSensitivity": zoom_sensitivity,
            "panSensitivity": pan_sensitivity,
            "panMouseButton": pan_mouse_button,
            "rotateMouseButton": rotate_mouse_button,
            "distance": distance,
            "minDistance": min_distance,
            "maxDistance": max_distance,
            "orthographicSize": orthographic_size,
            "minOrthographicSize": min_orthographic_size,
            "maxOrthographicSize": max_orthographic_size,
            "alpha": alpha,
            "beta": beta,
            "center": center,
            "minAlpha": min_alpha,
            "maxAlpha": max_alpha,
            "minBeta": min_beta,
            "maxBeta": max_beta,
            "animation": animation,
            "animationDurationUpdate": animation_duration_update,
            "animationEasingUpdate": animation_easing_update,
        }
