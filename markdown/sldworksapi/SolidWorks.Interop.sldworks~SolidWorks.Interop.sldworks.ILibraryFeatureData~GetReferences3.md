---
title: "GetReferences3 Method (ILibraryFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILibraryFeatureData"
member: "GetReferences3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~GetReferences3.html"
---

# GetReferences3 Method (ILibraryFeatureData)

Gets the references with respect to the specified scope.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetReferences3( _
   ByVal Scope As System.Integer, _
   ByRef RefType As System.Object, _
   ByRef RefName As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ILibraryFeatureData
Dim Scope As System.Integer
Dim RefType As System.Object
Dim RefName As System.Object
Dim value As System.Object

value = instance.GetReferences3(Scope, RefType, RefName)
```

### C#

```csharp
System.object GetReferences3(
   System.int Scope,
   out System.object RefType,
   out System.object RefName
)
```

### C++/CLI

```cpp
System.Object^ GetReferences3(
   System.int Scope,
   [Out] System.Object^ RefType,
   [Out] System.Object^ RefName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Scope`: Reference scope as defined in [swLibFeatureData_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLibFeatureData_e.html)
- `RefType`: Array of reference types as defined by [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)
- `RefName`: Array of reference names

### Return Value

Array of references

## VBA Syntax

See [LibraryFeatureData::GetReferences3](ms-its:sldworksapivb6.chm::/sldworks~LibraryFeatureData~GetReferences3.html).

## Examples

[Get Library Feature Data (VBA)](Get_Library_Feature_Data_Example_VB.htm)
[Get Library Feature Data (VB.NET)](Get_Library_Feature_Data_Example_VBNET.htm)
[Get Library Feature Data (C#)](Get_Library_Feature_Data_Example_CSharp.htm)

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[ILibraryFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData.html)
[ILibraryFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData_members.html)
[ILibraryFeatureData::SetReferences Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~SetReferences.html)
[ILibraryFeatureData::ISetReferences Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~ISetReferences.html)
[ILibraryFeatureData::IGetReferences3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~IGetReferences3.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
