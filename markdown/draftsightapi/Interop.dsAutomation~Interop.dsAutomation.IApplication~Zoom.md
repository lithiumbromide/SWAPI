---
title: "Zoom Method (IApplication)"
project: ""
interface: "IApplication"
member: "Zoom"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplication~Zoom.html"
---

# Zoom Method (IApplication)

Zooms to a region of the drawing determined by the specified range and entities.

## Syntax

### Visual Basic

```vb
Sub Zoom( _
   ByVal Range As dsZoomRange_e, _
   ByVal LowerLeftDblArray As System.Object, _
   ByVal UpperRightDblArray As System.Object _
)
```

### C#

```csharp
void Zoom(
   dsZoomRange_e Range,
   System.object LowerLeftDblArray,
   System.object UpperRightDblArray
)
```

### JScript

```
function Zoom(
   Range : dsZoomRange_e,
   LowerLeftDblArray : System.Object,
   UpperRightDblArray : System.Object
);
```

### Managed Extensions for C++

```
void Zoom(
   dsZoomRange_e Range,
   System.Object* LowerLeftDblArray,
   System.Object* UpperRightDblArray
)
```

### C++/CLI

```cpp
void Zoom(
   dsZoomRange_e Range,
   System.Object^ LowerLeftDblArray,
   System.Object^ UpperRightDblArray
)
```

### Parameters

- `Range`: Range as defined in [dsZoomRange_e](Interop.dsAutomation~Interop.dsAutomation.dsZoomRange_e.html)
- `LowerLeftDblArray`: Array of three doubles indicating the lower-left corner of the zoom area
- `UpperRightDblArray`: Array of three doubles indicating the upper-right corner of the zoom area

## Examples

[Create Angular Dimensions (C#)](Create_Angular_Dimensions_Example_CSharp.htm)
[Create Angular Dimensions (VB.NET)](Create_Angular_Dimensions_Example_VBNET.htm)
[Create Angular Dimensions (VBA)](Create_Angular_Dimensions_Example_VBA.htm)
[Mirror Entities (JavaScript)](Mirror_Entities_Example_JS.htm)
[Add and Modify Custom Data (JavaScript)](Add_and_Modify_Custom_Data_Example_JS.htm)

## See Also

[IApplication Interface](Interop.dsAutomation~Interop.dsAutomation.IApplication.html)
[IApplication Members](Interop.dsAutomation~Interop.dsAutomation.IApplication_members.html)
[IDocument::Pan Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~Pan.html)

## Availability

DraftSight V1R1.2
