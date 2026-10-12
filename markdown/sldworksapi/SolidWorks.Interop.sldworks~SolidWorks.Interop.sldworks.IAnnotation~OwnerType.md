---
title: "OwnerType Property (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "OwnerType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~OwnerType.html"
---

# OwnerType Property (IAnnotation)

Gets the type of owner of this annotation.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property OwnerType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
Dim value As System.Integer

instance.OwnerType = value

value = instance.OwnerType
```

### C#

```csharp
System.int OwnerType {get; set;}
```

### C++/CLI

```cpp
property System.int OwnerType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of owner of this annotation as defined in [swAnnotationOwner_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAnnotationOwner_e.html)

## VBA Syntax

See [Annotation::OwnerType](ms-its:sldworksapivb6.chm::/sldworks~Annotation~OwnerType.html).

## Remarks

Use this property to determine if an annotation is located on drawing view, drawing sheet, drawing template, assembly, or part. Use [IAnnotation::Owner](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~Owner.html) to gain access to the owner of the annotation.

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13
