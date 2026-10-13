---
title: "SetActive Method (ISwOLEObject)"
project: "SOLIDWORKS API Help"
interface: "ISwOLEObject"
member: "SetActive"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject~SetActive.html"
---

# SetActive Method (ISwOLEObject)

Activates or deactivates the OLE object.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetActive( _
   ByVal Active As System.Boolean _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISwOLEObject
Dim Active As System.Boolean
Dim value As System.Object

value = instance.SetActive(Active)
```

### C#

```csharp
System.object SetActive(
   System.bool Active
)
```

### C++/CLI

```cpp
System.Object^ SetActive(
   System.bool Active
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Active`: True activates the OLE object, false deactivates the OLE object

### Return Value

True gets the activated OLE object, false returns null

## VBA Syntax

See [SwOLEObject::SetActive](ms-its:sldworksapivb6.chm::/sldworks~SwOLEObject~SetActive.html).

## Examples

[Activate OLE Object (VBA)](Activate_OLE_Object_Example_VB.htm)

## See Also

[ISwOLEObject Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject.html)
[ISwOLEObject Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
