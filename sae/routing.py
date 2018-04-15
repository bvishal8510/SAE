from channels import include

channel_routing = [

    include("meter.routing.websocket_routing", path=r"^/chat/stream"),

    # include("talk.routing.custom_routing"),
]