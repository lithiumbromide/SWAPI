---
title: "ISensor Interface Members"
project: "SOLIDWORKS API Help"
interface: "ISensor_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor_members.html"
---

# ISensor Interface Members

The following tables list the members exposed by [ISensor](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | SensorAlertEnabled | Gets or sets whether an alert is triggered when the limits of the sensor deviate from its specified values. |
| Property | SensorAlertState | Gets whether an alert is currently triggered for this sensor. |
| Property | SensorAlertType | Gets or sets the type of alert for this sensor. |
| Property | SensorAlertValue1 | Gets or sets the alert value for this sensor. |
| Property | SensorAlertValue2 | Gets or sets alert value for this sensor; only in effect when sensor alert type set to swSensorAlert_Between. |
| Property | SensorType | Gets the type of this sensor. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | GetSensorFeatureData | Gets a sensor feature data. |
| Method | GetSensorValue | Gets the value and units of this sensor. |
| Method | UpdateSensor | Updates the sensor. |

[Top](#topBookmark)

## See Also

[ISensor Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IDimensionSensorData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionSensorData.html)
[DPartDocEvents_SensorAlertPreNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_SensorAlertPreNotifyEventHandler.html)
[DAssemblyDocEvents_SensorAlertPreNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_SensorAlertPreNotifyEventHandler.html)
