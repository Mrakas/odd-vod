_base_ = [
    '../../_base_/models/faster_rcnn_r50_dc5.py',
    '../../_base_/datasets/imagenet_vid_faster_rcnn_style.py',
    '../../_base_/default_runtime.py'
]
model = dict(
    type='SingleFasterRcnn')


# optimizer
optimizer = dict(type='SGD', lr=0.00375, momentum=0.9, weight_decay=0.0001)
optimizer_config = dict(
    _delete_=True, grad_clip=dict(max_norm=35, norm_type=2))
# learning policy
lr_config = dict(
    policy='step',
    warmup='linear',
    warmup_iters=500,
    warmup_ratio=1.0 / 3,
    step=[2, 5])
# runtime settings
total_epochs = 7
evaluation = dict(metric=['bbox'], interval=7)
fp16 = dict(loss_scale=512.)
    