---
title: "ShowInDocumentType Property (ICommandGroup)"
project: "SOLIDWORKS API Help"
interface: "ICommandGroup"
member: "ShowInDocumentType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~ShowInDocumentType.html"
---

# ShowInDocumentType Property (ICommandGroup)

Gets or sets the types of documents to show this CommandGroup.

## Syntax

### Visual Basic (Declaration)

```vb
Property ShowInDocumentType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICommandGroup
Dim value As System.Integer

instance.ShowInDocumentType = value

value = instance.ShowInDocumentType
```

### C#

```csharp
System.int ShowInDocumentType {get; set;}
```

### C++/CLI

```cpp
property System.int ShowInDocumentType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Types of documents in which to show this CommandGroup as defined in [swDocTemplateTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocTemplateTypes_e.html)

## VBA Syntax

See [CommandGroup::ShowInDocumentType](ms-its:sldworksapivb6.chm::/sldworks~CommandGroup~ShowInDocumentType.html).

## Examples

[Create Submenus in the CommandManager (C#)](Create_Submenus_in_the_CommandManager_Example_CSharp.htm)

## Remarks

This method only affects menus. The toolbar for the CommandGroup will be visible in every context, i.e., none, part, assembly, or drawing.

## See Also

[ICommandGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup.html)
[ICommandGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14
