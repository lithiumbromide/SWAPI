---
title: "MakeInterferingPartsTransparent Property (IInterferenceDetectionMgr)"
project: "SOLIDWORKS API Help"
interface: "IInterferenceDetectionMgr"
member: "MakeInterferingPartsTransparent"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~MakeInterferingPartsTransparent.html"
---

# MakeInterferingPartsTransparent Property (IInterferenceDetectionMgr)

Gets or sets whether to display the components of the selected interference in transparent mode.

## Syntax

### Visual Basic (Declaration)

```vb
Property MakeInterferingPartsTransparent As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IInterferenceDetectionMgr
Dim value As System.Boolean

instance.MakeInterferingPartsTransparent = value

value = instance.MakeInterferingPartsTransparent
```

### C#

```csharp
System.bool MakeInterferingPartsTransparent {get; set;}
```

### C++/CLI

```cpp
property System.bool MakeInterferingPartsTransparent {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to make interfering parts transparent, false to not

## VBA Syntax

See [InterferenceDetectionMgr::MakeInterferingPartsTransparent](ms-its:sldworksapivb6.chm::/sldworks~InterferenceDetectionMgr~MakeInterferingPartsTransparent.html).

## Examples

[Run Interference Detection (C#)](Run_Interference_Detection_Example_CSharp.htm)
[Run Interference Detection (VB.NET)](Run_Interference_Detection_Example_VBNET.htm)
[Run Interference Detection (VBA)](Run_Interference_Detection_Example_VB.htm)

## Remarks

Currently, the value set for this property:

- exists only while the InterferenceDetectionMgr object is in scope; i.e., setting this property is temporary.
- does not persist across SOLIDWORKS Design sessions.
- does not persist into the next invocation of interference detection in the user interface.

## See Also

[IInterferenceDetectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr.html)
[IInterferenceDetectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr_members.html)
[IInterferenceDetectionMgr::GetInterferenceComponentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~GetInterferenceComponentCount.html)
[IInterferenceDetectionMgr::GetInterferenceComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~GetInterferenceComponents.html)
[IInterferenceDetectionMgr::IGetInterferenceComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~IGetInterferenceComponents.html)
[IInterferenceDetectionMgr::NonInterferingComponentDisplay Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~NonInterferingComponentDisplay.html)
[IInterferenceDetectionMgr::TreatSubAssembliesAsComponents Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~TreatSubAssembliesAsComponents.html)
[IInterference::GetComponentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterference~GetComponentCount.html)
[IInterference::IGetComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterference~IGetComponents.html)
[IInterference::Components Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterference~Components.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
