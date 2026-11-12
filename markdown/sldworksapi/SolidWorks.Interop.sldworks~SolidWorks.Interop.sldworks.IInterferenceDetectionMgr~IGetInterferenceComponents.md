---
title: "IGetInterferenceComponents Method (IInterferenceDetectionMgr)"
project: "SOLIDWORKS API Help"
interface: "IInterferenceDetectionMgr"
member: "IGetInterferenceComponents"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~IGetInterferenceComponents.html"
---

# IGetInterferenceComponents Method (IInterferenceDetectionMgr)

Calculates and gets the interfering components.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetInterferenceComponents( _
   ByVal InterfernceComponentCount As System.Integer _
) As Component2
```

### Visual Basic (Usage)

```vb
Dim instance As IInterferenceDetectionMgr
Dim InterfernceComponentCount As System.Integer
Dim value As Component2

value = instance.IGetInterferenceComponents(InterfernceComponentCount)
```

### C#

```csharp
Component2 IGetInterferenceComponents(
   System.int InterfernceComponentCount
)
```

### C++/CLI

```cpp
Component2^ IGetInterferenceComponents(
   System.int InterfernceComponentCount
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `InterfernceComponentCount`: Number of interfering components

### Return Value

- in-process, unmanaged C++: Pointer to an array of interfering [components](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [IInteferenceDetectionMgr::GetInterferenceComponentCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IInterferenceDetectionMgr~GetInterferenceComponentCount.html) to get the size for the array of interfering components.

## See Also

[IInterferenceDetectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr.html)
[IInterferenceDetectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr_members.html)
[IInterferenceDetectionMgr::GetInterferenceComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~GetInterferenceComponents.html)
[IInterferenceDetectionMgr::MakeInterferingPartsTransparent Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~MakeInterferingPartsTransparent.html)
[IInterferenceDetectionMgr::NonInterferingComponentDisplay Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~NonInterferingComponentDisplay.html)
[IInterferenceDetectionMgr::TreatSubAssembliesAsComponents Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~TreatSubAssembliesAsComponents.html)
[IInterference::GetComponentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterference~GetComponentCount.html)
[IInterference::IGetComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterference~IGetComponents.html)
[IInterference::Components Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterference~Components.html)
[IInterferenceDetectionMgr::IGetComponentsTransformInterference Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~IGetComponentsTransformInterference.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
