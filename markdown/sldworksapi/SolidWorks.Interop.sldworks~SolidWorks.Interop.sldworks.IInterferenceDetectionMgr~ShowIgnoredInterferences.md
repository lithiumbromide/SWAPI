---
title: "ShowIgnoredInterferences Property (IInterferenceDetectionMgr)"
project: "SOLIDWORKS API Help"
interface: "IInterferenceDetectionMgr"
member: "ShowIgnoredInterferences"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~ShowIgnoredInterferences.html"
---

# ShowIgnoredInterferences Property (IInterferenceDetectionMgr)

Gets or sets whether to show ignored interferences.

## Syntax

### Visual Basic (Declaration)

```vb
Property ShowIgnoredInterferences As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IInterferenceDetectionMgr
Dim value As System.Boolean

instance.ShowIgnoredInterferences = value

value = instance.ShowIgnoredInterferences
```

### C#

```csharp
System.bool ShowIgnoredInterferences {get; set;}
```

### C++/CLI

```cpp
property System.bool ShowIgnoredInterferences {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to show ignored interferences, false to not

## VBA Syntax

See [InterferenceDetectionMgr::ShowIgnoredInterferences](ms-its:sldworksapivb6.chm::/sldworks~InterferenceDetectionMgr~ShowIgnoredInterferences.html).

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

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
