---
title: "Erased Property (IEmbeddedObject)"
project: ""
interface: "IEmbeddedObject"
member: "Erased"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IEmbeddedObject~Erased.html"
---

# Erased Property (IEmbeddedObject)

Gets or sets whether to erase or restore the embedded object.

## Syntax

### Visual Basic

```vb
Property Erased As System.Boolean
```

### C#

```csharp
System.bool Erased {get; set;}
```

### JScript

```
function get,set Erased : System.boolean
```

### Managed Extensions for C++

```
__property System.bool get_Erased();
__property void set_Erased(
   System.bool value
);
```

### C++/CLI

```cpp
property System.bool Erased {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to erase the embedded object, false to restore it (see **Remarks**)

## Examples

[Insert Embedded Object (C#)](Insert_Embedded_Object_Example_CSharp.htm)
[Insert Embedded Object (VB.NET)](Insert_Embedded_Object_Example_VBNET.htm)
[Insert Embedded Object (JavaScript)](Insert_Embedded_Object_Example_JS.htm)
[Insert Embedded Object (VBA)](Insert_Embedded_Object_Example_VBA.htm)

## Remarks

| If this property is set to true... | Then the embedded object... |
| --- | --- |
| and the drawing remains open | is not displayed and can be restored by setting this property to false. |
| when the drawing is closed | is deleted from the drawing and cannot be restored. |

## See Also

[IEmbeddedObject Interface](Interop.dsAutomation~Interop.dsAutomation.IEmbeddedObject.html)
[IEmbeddedObject Members](Interop.dsAutomation~Interop.dsAutomation.IEmbeddedObject_members.html)

## Availability

DraftSight V1R1.4
