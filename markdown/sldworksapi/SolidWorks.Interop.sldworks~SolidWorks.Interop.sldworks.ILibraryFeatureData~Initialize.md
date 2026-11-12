---
title: "Initialize Method (ILibraryFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILibraryFeatureData"
member: "Initialize"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~Initialize.html"
---

# Initialize Method (ILibraryFeatureData)

Initializes a newly created library feature using the specified library part.

## Syntax

### Visual Basic (Declaration)

```vb
Function Initialize( _
   ByVal FileNameIn As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ILibraryFeatureData
Dim FileNameIn As System.String
Dim value As System.Boolean

value = instance.Initialize(FileNameIn)
```

### C#

```csharp
System.bool Initialize(
   System.string FileNameIn
)
```

### C++/CLI

```cpp
System.bool Initialize(
   System.String^ FileNameIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileNameIn`: Path and filename of the library part

### Return Value

True if the library feature is initialized, false if not

## VBA Syntax

See [LibraryFeatureData::Initialize](ms-its:sldworksapivb6.chm::/sldworks~LibraryFeatureData~Initialize.html).

## Examples

[Create Library Feature With References (C#)](Create_Library_Feature_With_References_Example_CSharp.htm)
[Create Library Feature With References (VB.NET)](Create_Library_Feature_With_References_Example_VBNET.htm)
[Create Library Feature With References (VBA)](Create_Library_Feature_With_References_Example_VB.htm)

## See Also

[ILibraryFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData.html)
[ILibraryFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData_members.html)
[ILibraryFeatureData::LibraryPart Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~LibraryPart.html)
[ILibraryFeatureData::LinkToLibraryPart Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~LinkToLibraryPart.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
