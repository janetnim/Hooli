# Remember JSON.parse converts a json object into a dictionary while
# JSON.renderer converts a dictionary into a json object

import json
from rest_framework.renderers import JSONRenderer


class UserJSONRenderer(JSONRenderer):
  charset = 'utf-8'
  def render(self, data, media_type=None, renderer_context=None):
    # `token`` object come on form of bytes which normally does not serialize well
    # hence we need to decode it first
    return json.dumps({
        'user': data
      })
