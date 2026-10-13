---
title: "IGetComponents Method (ICavityFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICavityFeatureData"
member: "IGetComponents"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~IGetComponents.html"
---

# IGetComponents Method (ICavityFeatureData)

Gets the design components for this cavity feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub IGetComponents( _
   ByVal Count As System.Integer, _
   ByRef Comps As Component2 _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICavityFeatureData
Dim Count As System.Integer
Dim Comps As Component2

instance.IGetComponents(Count, Comps)
```

### C#

```csharp
void IGetComponents(
   System.int Count,
   out Component2 Comps
)
```

### C++/CLI

```cpp
void IGetComponents(
   System.int Count,
   [Out] Component2^ Comps
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of design components
- `Comps`: - in-process, unmanaged C++: Pointer to an array of [IComponent2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html) objects of size count

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [ICavityFeatureData::GetComponentsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICavityFeatureData~GetComponentsCount.html) before calling this method.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[ICavityFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData.html)
[ICavityFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData_members.html)
[ICavityFeatureData::ISetComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~ISetComponents.html)
[ICavityFeatureData::Components Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~Components.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13
