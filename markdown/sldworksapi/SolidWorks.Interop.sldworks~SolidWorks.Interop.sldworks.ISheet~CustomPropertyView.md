---
title: "CustomPropertyView Property (ISheet)"
project: "SOLIDWORKS API Help"
interface: "ISheet"
member: "CustomPropertyView"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~CustomPropertyView.html"
---

# CustomPropertyView Property (ISheet)

Gets or sets the drawing view to use to set the custom information for this drawing sheet.

## Syntax

### Visual Basic (Declaration)

```vb
Property CustomPropertyView As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISheet
Dim value As System.String

instance.CustomPropertyView = value

value = instance.CustomPropertyView
```

### C#

```csharp
System.string CustomPropertyView {get; set;}
```

### C++/CLI

```cpp
property System.String^ CustomPropertyView {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Name of the drawing view from which to get the custom information

## VBA Syntax

See [Sheet::CustomPropertyView](ms-its:sldworksapivb6.chm::/sldworks~Sheet~CustomPropertyView.html).

## Remarks

You can also use [IDrawingDoc::SetupSheet4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~SetupSheet4.html) to set the name of the drawing view to use to set the custom information for this drawing sheet.

## See Also

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.html)
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.html)

## Availability

SOLIDWORKS 2001Plus SP5, Revision Number 10.5
