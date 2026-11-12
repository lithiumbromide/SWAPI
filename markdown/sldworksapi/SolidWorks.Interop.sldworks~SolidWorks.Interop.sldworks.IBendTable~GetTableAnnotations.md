---
title: "GetTableAnnotations Method (IBendTable)"
project: "SOLIDWORKS API Help"
interface: "IBendTable"
member: "GetTableAnnotations"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendTable~GetTableAnnotations.html"
---

# GetTableAnnotations Method (IBendTable)

Gets the annotations for this bend table.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTableAnnotations() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBendTable
Dim value As System.Object

value = instance.GetTableAnnotations()
```

### C#

```csharp
System.object GetTableAnnotations()
```

### C++/CLI

```cpp
System.Object^ GetTableAnnotations();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [IBendTableAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBendTableAnnotation.html)s

## VBA Syntax

See [BendTable::GetTableAnnotations](ms-its:sldworksapivb6.chm::/sldworks~BendTable~GetTableAnnotations.html).

## See Also

[IBendTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendTable.html)
[IBendTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendTable_members.html)
[IBendTable::GetTableAnnotationCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendTable~GetTableAnnotationCount.html)
[IBendTable::IGetTableAnnotations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendTable~IGetTableAnnotations.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
