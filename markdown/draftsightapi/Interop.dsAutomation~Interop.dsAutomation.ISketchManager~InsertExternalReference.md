---
title: "InsertExternalReference Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "InsertExternalReference"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertExternalReference.html"
---

# InsertExternalReference Method (ISketchManager)

Inserts an external reference to a Block instance.

## Syntax

### Visual Basic

```vb
Function InsertExternalReference( _
   ByVal PathName As System.String, _
   ByVal InsertX As System.Double, _
   ByVal InsertY As System.Double, _
   ByVal InsertZ As System.Double, _
   ByVal Scale As System.Double, _
   ByVal Rotation As System.Double _
) As BlockInstance
```

### C#

```csharp
BlockInstance InsertExternalReference(
   System.string PathName,
   System.double InsertX,
   System.double InsertY,
   System.double InsertZ,
   System.double Scale,
   System.double Rotation
)
```

### JScript

```
function InsertExternalReference(
   PathName : System.String,
   InsertX : System.double,
   InsertY : System.double,
   InsertZ : System.double,
   Scale : System.double,
   Rotation : System.double
) : BlockInstance;
```

### Managed Extensions for C++

```
BlockInstance* InsertExternalReference(
   System.string* PathName,
   System.double InsertX,
   System.double InsertY,
   System.double InsertZ,
   System.double Scale,
   System.double Rotation
)
```

### C++/CLI

```cpp
BlockInstance^ InsertExternalReference(
   System.String^ PathName,
   System.double InsertX,
   System.double InsertY,
   System.double InsertZ,
   System.double Scale,
   System.double Rotation
)
```

### Parameters

- `PathName`: Path and file name of the external reference to insert
- `InsertX`: x coordinate where to insert the external reference
- `InsertY`: y coordinate where to insert the external reference
- `InsertZ`: z coordinate where to insert the external reference
- `Scale`: Scale factor for each axis
- `Rotation`: Angle by which to rotate the external reference; in radians (see **Remarks**)

### Return Value

External reference to a [Block instance](Interop.dsAutomation~Interop.dsAutomation.IBlockInstance.html)

## Examples

[Insert External Reference (C#)](Insert_External_Reference_Example_CSharp.htm)
[Insert External Reference (VB.NET)](Insert_External_Reference_Example_VBNET.htm)
[Insert External Reference (VBA)](Insert_External_Reference_Example_VBA.htm)

## Remarks

Use a positive value for Rotation to rotate the external reference counterclockwise and a negative value to rotate the external reference clockwise.

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::DetachExternalReference Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~DetachExternalReference.html)

## Availability

DraftSight V1R1
