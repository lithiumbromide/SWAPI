---
title: "FormToolConfiguration Property (ILibraryFormToolFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILibraryFormToolFeatureData"
member: "FormToolConfiguration"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData~FormToolConfiguration.html"
---

# FormToolConfiguration Property (ILibraryFormToolFeatureData)

Gets or sets the configuration of this forming tool's part to insert.

## Syntax

### Visual Basic (Declaration)

```vb
Property FormToolConfiguration As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ILibraryFormToolFeatureData
Dim value As System.String

instance.FormToolConfiguration = value

value = instance.FormToolConfiguration
```

### C#

```csharp
System.string FormToolConfiguration {get; set;}
```

### C++/CLI

```cpp
property System.String^ FormToolConfiguration {
   System.String^ get();
   void set (    System.String^ value);
}
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Property Value

Forming tool configuration name

## VBA Syntax

See

[LibraryFormToolFeatureData::FormToolConfiguration](ms-its:sldworksapivb6.chm::/sldworks~LibraryFormToolFeatureData~FormToolConfiguration.html)

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
