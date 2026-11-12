---
title: "LinkToFile Property (IDesignTable)"
project: "SOLIDWORKS API Help"
interface: "IDesignTable"
member: "LinkToFile"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~LinkToFile.html"
---

# LinkToFile Property (IDesignTable)

Gets or sets whether to link the design table to the model.

## Syntax

### Visual Basic (Declaration)

```vb
Property LinkToFile As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDesignTable
Dim value As System.Boolean

instance.LinkToFile = value

value = instance.LinkToFile
```

### C#

```csharp
System.bool LinkToFile {get; set;}
```

### C++/CLI

```cpp
property System.bool LinkToFile {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to link the design table to the model, false to not

## VBA Syntax

See [DesignTable::LinkToFile](ms-its:sldworksapivb6.chm::/sldworks~DesignTable~LinkToFile.html).

## Remarks

When a design table is linked to the model, any changes you make to the design table outside of the SOLIDWORKS Design software are reflected in the design table within the SOLIDWORKS Design model, and vice versa.

## See Also

[IDesignTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.html)
[IDesignTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable_members.html)
[IDesignTable::FileName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~FileName.html)
[IDesignTable::SourceType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~SourceType.html)
[IDesignTable::UpdateModel Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~UpdateModel.html)

## Availability

SOLIDWORKS 2004 SP3, Revision Number 12.3
