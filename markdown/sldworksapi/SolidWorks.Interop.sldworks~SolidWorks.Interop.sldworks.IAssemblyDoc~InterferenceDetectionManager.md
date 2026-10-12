---
title: "InterferenceDetectionManager Property (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "InterferenceDetectionManager"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~InterferenceDetectionManager.html"
---

# InterferenceDetectionManager Property (IAssemblyDoc)

Gets the Interference Detection manager, which allows you to run interference detection on an assembly to determine whether components interfere with each other.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property InterferenceDetectionManager As InterferenceDetectionMgr
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim value As InterferenceDetectionMgr

value = instance.InterferenceDetectionManager
```

### C#

```csharp
InterferenceDetectionMgr InterferenceDetectionManager {get;}
```

### C++/CLI

```cpp
property InterferenceDetectionMgr^ InterferenceDetectionManager {
   InterferenceDetectionMgr^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[IInterferenceDetectionMgr](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IInterferenceDetectionMgr.html)

## VBA Syntax

See [AssemblyDoc::InterferenceDetectionManager](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~InterferenceDetectionManager.html).

## Examples

[Run Interference Detection (C#)](Run_Interference_Detection_Example_CSharp.htm)
[Run Interference Detection (VB.NET)](Run_Interference_Detection_Example_VBNET.htm)
[Run Interference Detection (VBA)](Run_Interference_Detection_Example_VB.htm)
[Detect Interferences Using a Transform (VBA)](Detect_Interferences_Using_a_Transform_Example_VB.htm)
[Detect Interferences Using a Transform (VB.NET)](Detect_Interferences_Using_a_Transform_Example_VBNET.htm)
[Detect Interferences Using a Transform (C#)](Detect_Interferences_Using_a_Transform_Example_CSharp.htm)

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15
