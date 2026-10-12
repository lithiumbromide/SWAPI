---
title: "TreatCoincidenceAsInterference Property (IInterferenceDetectionMgr)"
project: "SOLIDWORKS API Help"
interface: "IInterferenceDetectionMgr"
member: "TreatCoincidenceAsInterference"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~TreatCoincidenceAsInterference.html"
---

# TreatCoincidenceAsInterference Property (IInterferenceDetectionMgr)

Gets or sets whether to treat coincident entities as interference.

## Syntax

### Visual Basic (Declaration)

```vb
Property TreatCoincidenceAsInterference As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IInterferenceDetectionMgr
Dim value As System.Boolean

instance.TreatCoincidenceAsInterference = value

value = instance.TreatCoincidenceAsInterference
```

### C#

```csharp
System.bool TreatCoincidenceAsInterference {get; set;}
```

### C++/CLI

```cpp
property System.bool TreatCoincidenceAsInterference {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to treat coincident entities as interference, false to not

## VBA Syntax

See [InterferenceDetectionMgr::TreatCoincidenceAsInterference](ms-its:sldworksapivb6.chm::/sldworks~InterferenceDetectionMgr~TreatCoincidenceAsInterference.html).

## Examples

[Run Interference Detection (C#)](Run_Interference_Detection_Example_CSharp.htm)
[Run Interference Detection (VB.NET)](Run_Interference_Detection_Example_VBNET.htm)
[Run Interference Detection (VBA)](Run_Interference_Detection_Example_VB.htm)
[Get Interferences Using a Transform (C#)](Detect_Interferences_Using_a_Transform_Example_CSharp.htm)
[Get Interferences Using a Transform (VB.NET)](Detect_Interferences_Using_a_Transform_Example_VBNET.htm)
[Get Interferences Using a Transform (VBA)](Detect_Interferences_Using_a_Transform_Example_VB.htm)

## Remarks

Currently, the value set for this property:

- exists only while the InterferenceDetectionMgr object is in scope; i.e., setting this property is temporary.
- does not persist across SOLIDWORKS Design sessions.
- does not persist into the next invocation of interference detection in the user interface.

## See Also

[IInterferenceDetectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr.html)
[IInterferenceDetectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
