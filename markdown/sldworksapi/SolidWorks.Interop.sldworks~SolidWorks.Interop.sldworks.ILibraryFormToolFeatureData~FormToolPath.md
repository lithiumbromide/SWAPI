---
title: "FormToolPath Property (ILibraryFormToolFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILibraryFormToolFeatureData"
member: "FormToolPath"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData~FormToolPath.html"
---

# FormToolPath Property (ILibraryFormToolFeatureData)

Gets or sets the pathname of this forming tool's part in the Design Library.

## Syntax

### Visual Basic (Declaration)

```vb
Property FormToolPath As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ILibraryFormToolFeatureData
Dim value As System.String

instance.FormToolPath = value

value = instance.FormToolPath
```

### C#

```csharp
System.string FormToolPath {get; set;}
```

### C++/CLI

```cpp
property System.String^ FormToolPath {
   System.String^ get();
   void set (    System.String^ value);
}
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Property Value

Design library forming tool part pathname

## VBA Syntax

See

[LibraryFormToolFeatureData::FormToolPath](ms-its:sldworksapivb6.chm::/sldworks~LibraryFormToolFeatureData~FormToolPath.html)

.

## Examples

See the

[ILibraryFormToolFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData.html)

examples.

## Remarks

When LibraryFormToolFeatureData is modified and this property changes to another forming tool, then the forming tool feature name changes to reflect the new forming tool name.

## See Also

[ILibraryFormToolFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData.html)

[ILibraryFormToolFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData_members.html)

## Availability

SOLIDWORKS 2025 SP02, Revision Number 33.2
