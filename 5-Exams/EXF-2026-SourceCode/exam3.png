[TITLE]

[OPTIONS]
FLOW_UNITS           CFS
INFILTRATION         CURVE_NUMBER
FLOW_ROUTING         DYNWAVE
START_DATE           05/10/2012
START_TIME           00:00:00
REPORT_START_DATE    05/10/2012
REPORT_START_TIME    00:00:00
END_DATE             05/11/2012
END_TIME             00:00:00
SWEEP_START          01/01
SWEEP_END            12/31
DRY_DAYS             0
REPORT_STEP          00:05:00
WET_STEP             00:05:00
DRY_STEP             00:05:00
ROUTING_STEP         0:00:30 
ALLOW_PONDING        NO
INERTIAL_DAMPING     NONE
VARIABLE_STEP        0.75
LENGTHENING_STEP     0
MIN_SURFAREA         0
NORMAL_FLOW_LIMITED  BOTH
SKIP_STEADY_STATE    NO
FORCE_MAIN_EQUATION  H-W
LINK_OFFSETS         DEPTH
MIN_SLOPE            0

[EVAPORATION]
;;Type       Parameters
;;---------- ----------
CONSTANT     0.0

[RAINGAGES]
;;               Rain      Time   Snow   Data      
;;Name           Type      Intrvl Catch  Source    
;;-------------- --------- ------ ------ ----------
1                INTENSITY 1:00   1.0    TIMESERIES Exam            

[SUBCATCHMENTS]
;;                                                 Total    Pcnt.             Pcnt.    Curb     Snow    
;;Name           Raingage         Outlet           Area     Imperv   Width    Slope    Length   Pack    
;;-------------- ---------------- ---------------- -------- -------- -------- -------- -------- --------
6                1                5                25       25       500      0.5      0                        
7                1                4                25       25       500      0.5      0                        
8                1                2                8        25       500      0.5      0                        
9                1                3                17       25       500      0.5      0                        

[SUBAREAS]
;;Subcatchment   N-Imperv   N-Perv     S-Imperv   S-Perv     PctZero    RouteTo    PctRouted 
;;-------------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
6                0.01       0.1        0.05       0.05       25         OUTLET    
7                0.01       0.1        0.05       0.05       25         OUTLET    
8                0.01       0.1        0.05       0.05       25         OUTLET    
9                0.01       0.1        0.05       0.05       25         OUTLET    

[INFILTRATION]
;;Subcatchment   CurveNum   HydCon     DryTime   
;;-------------- ---------- ---------- ----------
6                85         0.5        4         
7                85         0.5        4         
8                85         0.5        4         
9                85         0.5        4         

[JUNCTIONS]
;;               Invert     Max.       Init.      Surcharge  Ponded    
;;Name           Elev.      Depth      Depth      Depth      Area      
;;-------------- ---------- ---------- ---------- ---------- ----------
2                48         14         0          0          0         
3                56         10         0          0          0         
4                60         6          0          0          0         
5                65         5          0          0          0         

[OUTFALLS]
;;               Invert     Outfall    Stage/Table      Tide
;;Name           Elev.      Type       Time Series      Gate
;;-------------- ---------- ---------- ---------------- ----
1                35         FIXED      40               NO

[CONDUITS]
;;               Inlet            Outlet                      Manning    Inlet      Outlet     Init.      Max.      
;;Name           Node             Node             Length     N          Offset     Offset     Flow       Flow      
;;-------------- ---------------- ---------------- ---------- ---------- ---------- ---------- ---------- ----------
1                2                1                1000       0.015      0          0          0          0         
2                3                2                1000       0.015      0          2          0          0         
3                4                2                1000       0.015      0          2          0          0         
4                5                4                1000       0.015      0          0          0          0         

[XSECTIONS]
;;Link           Shape        Geom1            Geom2      Geom3      Geom4      Barrels   
;;-------------- ------------ ---------------- ---------- ---------- ---------- ----------
1                CIRCULAR     5                0          0          0          1                    
2                CIRCULAR     3                0          0          0          1                    
3                CIRCULAR     3                0          0          0          1                    
4                CIRCULAR     3                0          0          0          1                    

[LOSSES]
;;Link           Inlet      Outlet     Average    Flap Gate 
;;-------------- ---------- ---------- ---------- ----------

[TIMESERIES]
;;Name           Date       Time       Value     
;;-------------- ---------- ---------- ----------
Exam                        0:0        0         
Exam                        1          1         
Exam                        2          1         
Exam                        3          1         
Exam                        4          1         
Exam                        5          1         
Exam                        6          1         
Exam                        7          1         
Exam                        8          1         
Exam                        9          1         
Exam                        10         1         
Exam                        11         1         
Exam                        12         1         
Exam                        13         1         
Exam                        14         1         
Exam                        15         1         
Exam                        16         1         
Exam                        17         1         
Exam                        18         1         
Exam                        19         1         
Exam                        20         1         
Exam                        21         1         
Exam                        22         1         
Exam                        23         1         
Exam                        24         1         

[REPORT]
INPUT      NO
CONTROLS   NO
SUBCATCHMENTS ALL
NODES ALL
LINKS ALL

[TAGS]

[MAP]
DIMENSIONS 0.000 0.000 10000.000 10000.000
Units      None

[COORDINATES]
;;Node           X-Coord            Y-Coord           
;;-------------- ------------------ ------------------
2                7052.023           7842.004          
3                7167.630           3140.655          
4                2967.245           7842.004          
5                -404.624           7938.343          
1                9287.091           7822.736          

[VERTICES]
;;Link           X-Coord            Y-Coord           
;;-------------- ------------------ ------------------

[Polygons]
;;Subcatchment   X-Coord            Y-Coord           
;;-------------- ------------------ ------------------
6                -2042.389          8420.039          
6                -1946.050          5414.258          
6                1502.890           5337.187          
6                1464.355           8381.503          
6                -2100.193          8420.039          
7                1657.033           8400.771          
7                1734.104           5356.455          
7                4759.152           5221.580          
7                4816.956           8400.771          
7                1637.765           8420.039          
8                4971.098           6339.114          
8                8670.520           6204.239          
8                8689.788           8458.574          
8                4971.098           8439.306          
9                5240.848           1488.439          
9                8824.663           1353.565          
9                8747.592           6112.717          
9                5009.634           6151.252          

[SYMBOLS]
;;Gage           X-Coord            Y-Coord           
;;-------------- ------------------ ------------------
1                -2639.692          9421.965          

