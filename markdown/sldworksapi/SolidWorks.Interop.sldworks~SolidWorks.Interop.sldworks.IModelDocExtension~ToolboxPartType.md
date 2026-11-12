---
title: "ToolboxPartType Property (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "ToolboxPartType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ToolboxPartType.html"
---

# ToolboxPartType Property (IModelDocExtension)

Gets and sets whether this part is a SOLIDWORKS Toolbox part.

## Syntax

### Visual Basic (Declaration)

```vb
Property ToolboxPartType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As System.Integer

instance.ToolboxPartType = value

value = instance.ToolboxPartType
```

### C#

```csharp
System.int ToolboxPartType {get; set;}
```

### C++/CLI

```cpp
property System.int ToolboxPartType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of SOLIDWORKS Toolbox part type as defined in [swToolBoxPartType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swToolBoxPartType_e.html)

## VBA Syntax

See [ModelDocExtension::ToolBoxPartType](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~ToolBoxPartType.html).

## Examples

[Test for Toolbox Part (VBA)](Test_For_Toolbox_Part_Example_VB.htm)
[Test for Toolbox Part (VB.NET)](Test_for_Toolbox_Part_Example_VBNET.htm)
[Test for Toolbox Part (C#)](Test_for_Toolbox_Part_Example_CSharp.htm)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
