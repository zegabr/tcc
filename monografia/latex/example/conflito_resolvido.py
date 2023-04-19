# ========================== diff3 result ==========================
(...)
 def _smooth_labels():
    num_classes = math_ops.cast(array_ops.shape(y_true)[-1], y_pred.dtype)
    return y_true * (1.0 - label_smoothing) + (label_smoothing / num_classes)

<<<<<<< left.py
  y_true = smart_cond.smart_cond(
      label_smoothing, _smooth_labels, lambda: y_true)
  return K.categorical_crossentropy(y_true, y_pred, from_logits=from_logits, axis=axis)
=======
# CResolvido
  y_true = smart_cond.smart_cond(label_smoothing, _smooth_labels,
                                 lambda: y_true)
  return K.categorical_crossentropy(y_true, y_pred, from_logits=from_logits)
>>>>>>> right.py
(...)
# ========================== csdiff result =========================
(...)
  def _smooth_labels():
    num_classes = math_ops.cast(array_ops.shape(y_true)[-1], y_pred.dtype)
    return y_true * (1.0 - label_smoothing) + (label_smoothing / num_classes)

  y_true = smart_cond.smart_cond(label_smoothing, _smooth_labels,
                                 lambda: y_true)
  return K.categorical_crossentropy(y_true, y_pred, from_logits=from_logits, axis=axis)
(...)
