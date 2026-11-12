---
title: "IGetComponents Method (IInterference)"
project: "SOLIDWORKS API Help"
interface: "IInterference"
member: "IGetComponents"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterference~IGetComponents.html"
---

# IGetComponents Method (IInterference)

Gets the components that interfere with each other.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetComponents( _
   ByVal ComponentCount As System.Integer _
) As Component2
```

### Visual Basic (Usage)

```vb
Dim instance As IInterference
Dim ComponentCount As System.Integer
Dim value As Component2

value = instance.IGetComponents(ComponentCount)
```

### C#

```csharp
Component2 IGetComponents(
   System.int ComponentCount
)
```

### C++/CLI

```cpp
Component2^ IGetComponents(
   System.int ComponentCount
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ComponentCount`: Number of components interfering with each other

### Return Value

- in-process, unmanaged C++: Pointer to an array of [components](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html) interfering with each other

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [IInterference::GetComponentCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IInterference~GetComponentCount.html) before calling this method to determine the size of the array.

## See Also

[IInterference Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterference.html)
[IInterference Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterference_members.html)
[IInterference::Components Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterference~Components.html)
[IInterferenceDetectionMgr::GetInterferenceComponentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~GetInterferenceComponentCount.html)
[IInterferenceDetectionMgr::GetInterferenceComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~GetInterferenceComponents.html)
[IInterferenceDetectionMgr::IGetInterferenceComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~IGetInterferenceComponents.html)
[IInterferenceDetectionMgr::MakeInterferingPartsTransparent Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~MakeInterferingPartsTransparent.html)
[IInterferenceDetectionMgr::NonInterferingComponentDisplay Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~NonInterferingComponentDisplay.html)
[IInterferenceDetectionMgr::TreatSubAssembliesAsComponents Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~TreatSubAssembliesAsComponents.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
