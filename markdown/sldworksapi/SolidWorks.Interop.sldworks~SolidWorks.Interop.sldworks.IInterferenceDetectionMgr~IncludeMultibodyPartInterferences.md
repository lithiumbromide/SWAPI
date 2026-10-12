---
title: "IncludeMultibodyPartInterferences Property (IInterferenceDetectionMgr)"
project: "SOLIDWORKS API Help"
interface: "IInterferenceDetectionMgr"
member: "IncludeMultibodyPartInterferences"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~IncludeMultibodyPartInterferences.html"
---

# IncludeMultibodyPartInterferences Property (IInterferenceDetectionMgr)

Gets or sets whether to report interferences between bodies within multibody parts.

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeMultibodyPartInterferences As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IInterferenceDetectionMgr
Dim value As System.Boolean

instance.IncludeMultibodyPartInterferences = value

value = instance.IncludeMultibodyPartInterferences
```

### C#

```csharp
System.bool IncludeMultibodyPartInterferences {get; set;}
```

### C++/CLI

```cpp
property System.bool IncludeMultibodyPartInterferences {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to report interferences between bodies within multibody parts, false to not

## VBA Syntax

See [InterferenceDetectionMgr::IncludeMultibodyPartInterferences](ms-its:sldworksapivb6.chm::/sldworks~InterferenceDetectionMgr~IncludeMultibodyPartInterferences.html).

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
