---
title: "IGetComponentsTransformInterference Method (IInterferenceDetectionMgr)"
project: "SOLIDWORKS API Help"
interface: "IInterferenceDetectionMgr"
member: "IGetComponentsTransformInterference"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~IGetComponentsTransformInterference.html"
---

# IGetComponentsTransformInterference Method (IInterferenceDetectionMgr)

Calculates and gets the interfering components for the specified components and math transform.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetComponentsTransformInterference( _
   ByVal NumOfComponent As System.Integer, _
   ByRef Component As Component2, _
   ByRef Transform As MathTransform, _
   ByVal NumOfIntComponent As System.Integer, _
   ByRef InterferingComponent As Component2 _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IInterferenceDetectionMgr
Dim NumOfComponent As System.Integer
Dim Component As Component2
Dim Transform As MathTransform
Dim NumOfIntComponent As System.Integer
Dim InterferingComponent As Component2
Dim value As System.Boolean

value = instance.IGetComponentsTransformInterference(NumOfComponent, Component, Transform, NumOfIntComponent, InterferingComponent)
```

### C#

```csharp
System.bool IGetComponentsTransformInterference(
   System.int NumOfComponent,
   ref Component2 Component,
   ref MathTransform Transform,
   System.int NumOfIntComponent,
   out Component2 InterferingComponent
)
```

### C++/CLI

```cpp
System.bool IGetComponentsTransformInterference(
   System.int NumOfComponent,
   Component2^% Component,
   MathTransform^% Transform,
   System.int NumOfIntComponent,
   [Out] Component2^ InterferingComponent
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumOfComponent`: Number of components in array specified by Component
- `Component`: - in-process, unmanaged C++: Pointer to an array of [components](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html)

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.
- `Transform`: [IMathTransform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathTransform.html)
- `NumOfIntComponent`: Number of interfering components in array returned by this method (see **Remarks**)
- `InterferingComponent`: - in-process, unmanaged C++: Pointer to an array of interfering [components](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html)

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

### Return Value

True if successful, false if not

## Remarks

Before calling this method, call [IInterferenceDetectionMgr::GetComponentsTransformInterferenceCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IInterferenceDetectionMgr~GetComponentsTransformInterferenceCount.html) to populate NumOfIntComponent.

## See Also

[IInterferenceDetectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr.html)
[IInterferenceDetectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr_members.html)
[IInterferenceDetectionMgr::GetComponentsTransformInterference Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~GetComponentsTransformInterference.html)
[IInterferenceDetectionMgr::CreateFastenersFolder Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~CreateFastenersFolder.html)
[IInterferenceDetectionMgr::IgnoreHiddenBodies Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~IgnoreHiddenBodies.html)
[IInterferenceDetectionMgr::IncludeMultibodyPartInterferences Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~IncludeMultibodyPartInterferences.html)
[IInterferenceDetectionMgr::MakeInterferingPartsTransparent Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~MakeInterferingPartsTransparent.html)
[IInterferenceDetectionMgr::NonInterferingComponentDisplay Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~NonInterferingComponentDisplay.html)
[IInterferenceDetectionMgr::ShowIgnoredInterferences Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~ShowIgnoredInterferences.html)
[IInterferenceDetectionMgr::TreatCoincidenceAsInterference Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~TreatCoincidenceAsInterference.html)
[IInterferenceDetectionMgr::TreatSubAssembliesAsComponents Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~TreatSubAssembliesAsComponents.html)
[IInterferenceDetectionMgr::IGetInterferenceComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~IGetInterferenceComponents.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
