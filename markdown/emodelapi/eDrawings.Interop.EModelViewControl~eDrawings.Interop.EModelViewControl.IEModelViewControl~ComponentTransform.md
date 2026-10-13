---
title: "ComponentTransform Property (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "ComponentTransform"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ComponentTransform.html"
---

# ComponentTransform Property (IEModelViewControl)

Gets or sets the transform for the specified component.

## Syntax

### Visual Basic (Declaration)

```vb
Property ComponentTransform( _
   ByVal ComponentName As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim ComponentName As System.String
Dim value As System.Object

instance.ComponentTransform(ComponentName) = value

value = instance.ComponentTransform(ComponentName)
```

### C#

```csharp
System.object ComponentTransform(
   System.string ComponentName
) {get; set;}
```

### C++/CLI

```cpp
property System.Object^ ComponentTransform {
   System.Object^ get(System.String^ ComponentName);
   void set (System.String^ ComponentName, System.Object^ value);
}
```

### Parameters

- `ComponentName`: Name of the component

### Property Value

Transform (see **Remarks**)

## VBA Syntax

See [EModelViewControl::ComponentTransform](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~ComponentTransform.html).

## Remarks

The eDrawings transformation matrix is stored as a homogeneous matrix of 16 elements:

|a b c . n |

|d e f . o |

|g h i . p |

|j k l . m |

The first 9 elements (a to i) are elements of a 3x3 rotational sub-matrix, the next 3 elements (j,k,l) define a translation vector, and the next 1 element (m) is a scaling factor. The last 3 elements (n,o,p) are unused in this context.

The 3x3 rotational sub-matrix represents 3 axis sets:

- row 1 for x-axis components of rotation
- row 2 for y-axis components of rotation
- row 3 for z-axis components of rotation

The 3 axes are constrained to be orthogonal and unified so that they produce a pure rotational transformation. Reflections can also be added to these axes by setting the components to negative. The rotation sub-matrix, coupled with the lower-left translation vector and the lower-right corner scaling factor, creates an affine transformation, which is a transformation that preserves lines and parallelism, i.e., maps parallel lines to parallel lines.

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)
[IEModelViewControl::ComponentConfigurationName Property ()](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ComponentConfigurationName.html)
[IEModelViewControl::ComponentCount Property ()](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ComponentCount.html)
[IEModelViewControl::ComponentName Property ()](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ComponentName.html)
[IEModelViewControl::ComponentState Property ()](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ComponentState.html)
[IEModelViewControl::GetSelectedComponentName Method ()](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~GetSelectedComponentName.html)

## Availability

eDrawings API 2014 SP0
