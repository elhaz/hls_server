from django.shortcuts import render
from django.http import HttpResponse



def hls_view(request, cam_num:str, filename:str='index.m3u8'):
    print(f'cam_num: {cam_num}, filename: {filename}')
    filepath = f'video/{cam_num}/{filename}'
    with open(filepath, 'rb') as f:
        content = f.read()
    if filename.endswith('.m3u8'):
        return HttpResponse(content, content_type='application/vnd.apple.mpegurl')
    elif filename.endswith('.ts'):
        return HttpResponse(content, content_type='video/MP2T')
    else :
        return HttpResponse(content, content_type='application/octet-stream')