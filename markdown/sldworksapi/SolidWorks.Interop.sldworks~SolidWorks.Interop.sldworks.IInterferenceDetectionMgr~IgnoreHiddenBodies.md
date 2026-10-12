---
title: "IgnoreHiddenBodies Property (IInterferenceDetectionMgr)"
project: "SOLIDWORKS API Help"
interface: "IInterferenceDetectionMgr"
member: "IgnoreHiddenBodies"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~IgnoreHiddenBodies.html"
---

# IgnoreHiddenBodies Property (IInterferenceDetectionMgr)

Gets or sets whether to ignore hidden bodies during interference detection.

## Syntax

### Visual Basic (Declaration)

```vb
Property IgnoreHiddenBodies As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IInterferenceDetectionMgr
Dim value As System.Boolean

instance.IgnoreHiddenBodies = value

value = instance.IgnoreHiddenBodies
```

### C#

```csharp
System.bool IgnoreHiddenBodies {get; set;}
```

### C++/CLI

```cpp
property System.bool IgnoreHiddenBodies {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to ignore hidden bodies, false to not

## VBA Syntax

See [InterferenceDetectionMgr::IgnoreHiddenBodies](ms-its:sldworksapivb6.chm::/sldworks~InterferenceDetectionMgr~IgnoreHiddenBodies.html).

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

SOLIDWORKS 2011 FCS, Revision Number 19.0
