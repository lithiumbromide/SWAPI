---
title: "ISetComponents Method (ICavityFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICavityFeatureData"
member: "ISetComponents"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~ISetComponents.html"
---

# ISetComponents Method (ICavityFeatureData)

Sets the design components for this cavity feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetComponents( _
   ByVal Count As System.Integer, _
   ByRef Comps As Component2 _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICavityFeatureData
Dim Count As System.Integer
Dim Comps As Component2

instance.ISetComponents(Count, Comps)
```

### C#

```csharp
void ISetComponents(
   System.int Count,
   ref Component2 Comps
)
```

### C++/CLI

```cpp
void ISetComponents(
   System.int Count,
   Component2^% Comps
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of design components
- `Comps`: - in-process, unmanaged C++: Pointer to an array of [IComponent2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html) objects of size Count

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## VBA Syntax

See [CavityFeatureData::ISetComponents](ms-its:sldworksapivb6.chm::/sldworks~CavityFeatureData~ISetComponents.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[ICavityFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData.html)
[ICavityFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData_members.html)
[ICavityFeatureData::IGetComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~IGetComponents.html)
[ICavityFeatureData::GetComponentsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~GetComponentsCount.html)
[ICavityFeatureData::Components Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~Components.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13
