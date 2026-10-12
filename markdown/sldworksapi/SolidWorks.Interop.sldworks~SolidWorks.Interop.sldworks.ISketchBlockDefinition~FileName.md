---
title: "FileName Property (ISketchBlockDefinition)"
project: "SOLIDWORKS API Help"
interface: "ISketchBlockDefinition"
member: "FileName"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~FileName.html"
---

# FileName Property (ISketchBlockDefinition)

Gets or sets the name of the file to which the block definition is linked.

## Syntax

### Visual Basic (Declaration)

```vb
Property FileName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchBlockDefinition
Dim value As System.String

instance.FileName = value

value = instance.FileName
```

### C#

```csharp
System.string FileName {get; set;}
```

### C++/CLI

```cpp
property System.String^ FileName {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Path and filename of the block definition file

## VBA Syntax

See [SketchBlockDefinition::FileName](ms-its:sldworksapivb6.chm::/sldworks~SketchBlockDefinition~FileName.html).

## Remarks

The file can be either a native SOLIDWORKS block file (.sldblk) or a non-native SOLIDWORKS file (.dxf or .dwg).

This method gets the name of the file with which this block definition is associated, regardless of whether or not the link is enabled. SOLIDWORKS continues to store the name of the file if the link is disabled. Use [ISketchBlockDefintion::LinkToFile](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockDefinition~LinkToFile.html) to determine if the block definition is linked to a file.

## See Also

[ISketchBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.html)
[ISketchBlockDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition_members.html)
[ISketchBlockDefinition::Save Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~Save.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
