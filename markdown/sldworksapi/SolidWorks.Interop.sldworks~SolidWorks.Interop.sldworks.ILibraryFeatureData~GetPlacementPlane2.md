---
title: "GetPlacementPlane2 Method (ILibraryFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILibraryFeatureData"
member: "GetPlacementPlane2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~GetPlacementPlane2.html"
---

# GetPlacementPlane2 Method (ILibraryFeatureData)

Gets the face or plane on which the library feature was placed.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPlacementPlane2( _
   ByVal Scope As System.Integer, _
   ByRef Type As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ILibraryFeatureData
Dim Scope As System.Integer
Dim Type As System.Integer
Dim value As System.Object

value = instance.GetPlacementPlane2(Scope, Type)
```

### C#

```csharp
System.object GetPlacementPlane2(
   System.int Scope,
   out System.int Type
)
```

### C++/CLI

```cpp
System.Object^ GetPlacementPlane2(
   System.int Scope,
   [Out] System.int Type
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Scope`: Placement scope as defined in [swLibFeatureData_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLibFeatureData_e.html)
- `Type`: Placement type as defined in [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

### Return Value

[Face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) or [plane](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefPlane.html)

## VBA Syntax

See [LibraryFeatureData::GetPlacementPlane2](ms-its:sldworksapivb6.chm::/sldworks~LibraryFeatureData~GetPlacementPlane2.html).

## Examples

[Get Library Feature Data (VBA)](Get_Library_Feature_Data_Example_VB.htm)
[Get Library Feature Data (VB.NET)](Get_Library_Feature_Data_Example_VBNET.htm)
[Get Library Feature Data (C#)](Get_Library_Feature_Data_Example_CSharp.htm)

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[ILibraryFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData.html)
[ILibraryFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData_members.html)
[ILibraryFeatureData::SetPlacementPlane Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~SetPlacementPlane.html)

## Availability

SOLIDWORKS 2010 SP1, Revision Number 18.1
