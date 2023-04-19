# ========================== diff3 result ==========================
(...)
        # TextBox's text object should not parse mathtext at all.
        self.text_disp = self.ax.text(
<<<<<<< left.py
            self.DIST, 0.5, initial, transform=self.ax.transAxes,
            verticalalignment='center', horizontalalignment=ha)
=======
            self.DIST_FROM_LEFT, 0.5, initial,
            transform=self.ax.transAxes, verticalalignment='center',
            horizontalalignment='left', parse_math=False)
>>>>>>> right.py

        self._observers = cbook.CallbackRegistry()
(...)
# ========================== csdiff result =========================
(...)
        # TextBox's text object should not parse mathtext at all.
        self.text_disp = self.ax.text(
            self.DIST, 0.5, initial,
            transform=self.ax.transAxes, verticalalignment='center',
            horizontalalignment='left', # CaFN
<<<<<<< left.py
 horizontalalignment=ha
=======
# CReduzido
 parse_math=False
>>>>>>> right.py
)

        self._observers = cbook.CallbackRegistry()
(...)
