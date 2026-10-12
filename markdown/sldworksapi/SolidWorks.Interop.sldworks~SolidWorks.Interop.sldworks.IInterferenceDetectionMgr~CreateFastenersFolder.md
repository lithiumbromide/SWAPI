---
title: "CreateFastenersFolder Property (IInterferenceDetectionMgr)"
project: "SOLIDWORKS API Help"
interface: "IInterferenceDetectionMgr"
member: "CreateFastenersFolder"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~CreateFastenersFolder.html"
---

# CreateFastenersFolder Property (IInterferenceDetectionMgr)

Gets or sets whether to create the Fasteners folders to segregate interferences involving fasteners.

## Syntax

### Visual Basic (Declaration)

```vb
Property CreateFastenersFolder As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IInterferenceDetectionMgr
Dim value As System.Boolean

instance.CreateFastenersFolder = value

value = instance.CreateFastenersFolder
```

### C#

```csharp
System.bool CreateFastenersFolder {get; set;}
```

### C++/CLI

```cpp
property System.bool CreateFastenersFolder {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to create fasteners folder, false to not

## VBA Syntax

See [InterferenceDetectionMgr::CreateFastenersFolder](ms-its:sldworksapivb6.chm::/sldworks~InterferenceDetectionMgr~CreateFastenersFolder.html).

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
[IInterference::IsFastener Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterference~IsFastener.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
