---
title: "LinkToFormTool Property (ILibraryFormToolFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILibraryFormToolFeatureData"
member: "LinkToFormTool"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData~LinkToFormTool.html"
---

# LinkToFormTool Property (ILibraryFormToolFeatureData)

Gets or sets whether to link this forming tool to its part in the Design Library.

## Syntax

### Visual Basic (Declaration)

```vb
Property LinkToFormTool As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ILibraryFormToolFeatureData
Dim value As System.Boolean

instance.LinkToFormTool = value

value = instance.LinkToFormTool
```

### C#

```csharp
System.bool LinkToFormTool {get; set;}
```

### C++/CLI

```cpp
property System.bool LinkToFormTool {
   System.bool get();
   void set (    System.bool value);
}
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Property Value

True to link this forming tool to its part in the Design Library, false to not

## VBA Syntax

See

[LibraryFormToolFeatureData::LinkToFormTool](ms-its:sldworksapivb6.chm::/sldworks~LibraryFormToolFeatureData~LinkToFormTool.html)

.

## Examples

See the

[ILibraryFormToolFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData.html)

examples.

## See Also

[ILibraryFormToolFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData.html)

[ILibraryFormToolFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData_members.html)

## Availability

SOLIDWORKS 2025 SP02, Revision Number 33.2
