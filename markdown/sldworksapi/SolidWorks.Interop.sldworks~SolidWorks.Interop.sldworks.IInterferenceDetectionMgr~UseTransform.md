---
title: "UseTransform Property (IInterferenceDetectionMgr)"
project: "SOLIDWORKS API Help"
interface: "IInterferenceDetectionMgr"
member: "UseTransform"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~UseTransform.html"
---

# UseTransform Property (IInterferenceDetectionMgr)

Gets or sets whether to use transforms in interference detection.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseTransform As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IInterferenceDetectionMgr
Dim value As System.Boolean

instance.UseTransform = value

value = instance.UseTransform
```

### C#

```csharp
System.bool UseTransform {get; set;}
```

### C++/CLI

```cpp
property System.bool UseTransform {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to use transforms, false to not

## VBA Syntax

See [InterferenceDetectionMgr::UseTransform](ms-its:sldworksapivb6.chm::/sldworks~InterferenceDetectionMgr~UseTransform.html).

## Examples

[Run Interference Detection (VBA)](Run_Interference_Detection_Example_VB.htm)
[Run Interference Detection (VB.NET)](Run_Interference_Detection_Example_VBNET.htm)
[Run Interference Detection (C#)](Run_Interference_Detection_Example_CSharp.htm)

## See Also

[IInterferenceDetectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr.html)
[IInterferenceDetectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
