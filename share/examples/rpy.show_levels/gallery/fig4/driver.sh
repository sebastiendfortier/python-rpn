# Load cmoi base ssm domaine
rpy.show_levels -i \
   $CMCGRIDF/prog/glbhyb/$(date +%Y%m%d00)_000\
   $CMCGRIDF/prog/reghyb/$(date +%Y%m%d00)_000\
   $CMCGRIDF/prog/lam/nat.model/$(date +%Y%m%d00)_000\
   --vcode\
   --title ETIKET\
   --small_scale_topo_amp 0.\
   --out fig4.png
