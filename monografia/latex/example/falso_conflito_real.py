# ========================== diff3 result ==========================
(...)
       if np.ndim(data) == 0 and isinstance(self, ScalarMappable):
            # This block logically belongs to ScalarMappable, but can't be
            # implemented in it because most ScalarMappable subclasses inherit
            # from Artist first and from ScalarMappable second, so
            # Artist.format_cursor_data would always have precedence over
            # ScalarMappable.format_cursor_data.
            n = self.cmap.N
            if np.ma.getmask(data):
                return "[]"
            normed = self.norm(data)
            if np.isfinite(normed):
                # Midpoints of neighboring color intervals.
                neighbors = self.norm.inverse(
                    (int(self.norm(data) * n) + np.array([0, 1])) / n)
                delta = abs(neighbors - data).max()
(...)
# ========================== csdiff result =========================
(...)
        if np.ndim(data) == 0 and isinstance(self, ScalarMappable):
            # This block logically belongs to ScalarMappable, but can't be
            # implemented in it because most ScalarMappable subclasses inherit
            # from Artist first and from ScalarMappable second, so
            # Artist.format_cursor_data would always have precedence over
            # ScalarMappable.format_cursor_data.
            n = self.cmap.N
            if np.ma.getmask(data):
                return "[]"
<<<<<<< left.py
            normed = self.norm(data)
            if np.isfinite(normed):
                # Midpoints of neighboring color intervals.
                neighbors = self.norm.inverse
# FCR
=======
            normed = self.norm
>>>>>>> right.py
(data)
<<<<<<< left.py
                    (int(self.norm
=======
# FCR
            if np.isfinite(normed):
                # Midpoints of neighboring color intervals.
                neighbors = self.norm.inverse(
                    (int(self.norm
>>>>>>> right.py
(data) * n) + np.array([0, 1])) / n)
                delta = abs(neighbors - data).max()
(...)
