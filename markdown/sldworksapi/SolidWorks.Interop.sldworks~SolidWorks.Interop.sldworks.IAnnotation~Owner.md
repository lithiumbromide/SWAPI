---
title: "Owner Property (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "Owner"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~Owner.html"
---

# Owner Property (IAnnotation)

Gets the owner of this annotation.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property Owner As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
Dim value As System.Object

instance.Owner = value

value = instance.Owner
```

### C#

```csharp
System.object Owner {get; set;}
```

### C++/CLI

```cpp
property System.Object^ Owner {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Object for the view, sheet, or model document

## VBA Syntax

See [Annotation::Owner](ms-its:sldworksapivb6.chm::/sldworks~Annotation~Owner.html).

## Remarks

Use [IAnnotation::OwnerType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~OwnerType.html) to determine if the annotation is located on a drawing view, drawing sheet, drawing template, assembly, or part.

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13
