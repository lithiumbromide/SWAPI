---
title: "GetExtractionDirection Method (ICoreFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICoreFeatureData"
member: "GetExtractionDirection"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData~GetExtractionDirection.html"
---

# GetExtractionDirection Method (ICoreFeatureData)

Gets the entities that define the extraction direction of this core feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetExtractionDirection( _
   ByRef Type1 As System.Integer, _
   ByRef PDir1 As System.Object, _
   ByRef Type2 As System.Integer, _
   ByRef PDir2 As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICoreFeatureData
Dim Type1 As System.Integer
Dim PDir1 As System.Object
Dim Type2 As System.Integer
Dim PDir2 As System.Object
Dim value As System.Integer

value = instance.GetExtractionDirection(Type1, PDir1, Type2, PDir2)
```

### C#

```csharp
System.int GetExtractionDirection(
   out System.int Type1,
   out System.object PDir1,
   out System.int Type2,
   out System.object PDir2
)
```

### C++/CLI

```cpp
System.int GetExtractionDirection(
   [Out] System.int Type1,
   [Out] System.Object^ PDir1,
   [Out] System.int Type2,
   [Out] System.Object^ PDir2
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Type1`: Type of entity as defined in [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)
- `PDir1`: Entity that defines the extraction direction (see **Remarks**)
- `Type2`: Type of entity as defined in [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)
- `PDir2`: Entity that defines the extraction direction (see Remarks)

### Return Value

Number of entities that define the extraction direction

## VBA Syntax

See [CoreFeatureData::GetExtractionDirection](ms-its:sldworksapivb6.chm::/sldworks~CoreFeatureData~GetExtractionDirection.html).

## Examples

[Get Core Feature Data (C#)](Get_Core_Feature_Example_CSharp.htm)
[Get Core Feature Data (VB.NET)](Get_Core_Feature_Example_VBNET.htm)
[Get Core Feature Data (VBA)](Get_Core_Feature_Example_VB.htm)

## Remarks

The types of entities that define the extraction direction are:

- Face
- Plane
- Edge
- Vertex
- Sketch line
- Sketch point

There can be two entities because two sketch points can specify a direction.

## See Also

[ICoreFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData.html)
[ICoreFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData_members.html)
[ICoreFeatureData::SetExtractionDirection Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData~SetExtractionDirection.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
