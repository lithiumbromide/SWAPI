---
title: "InsertAttributeDefinition2 Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "InsertAttributeDefinition2"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertAttributeDefinition2.html"
---

# InsertAttributeDefinition2 Method (ISketchManager)

Creates a BlockAttribute definition.

## Syntax

### Visual Basic

```vb
Function InsertAttributeDefinition2( _
   ByVal Name As System.String, _
   ByVal Caption As System.String, _
   ByVal DefaultValue As System.String, _
   ByVal PositionX As System.Double, _
   ByVal PositionY As System.Double, _
   ByVal PositionZ As System.Double, _
   ByVal TextStyle As System.String, _
   ByVal Justification As dsTextJustification_e, _
   ByVal Height As System.Double, _
   ByVal Rotation As System.Double, _
   ByVal Fixed As System.Boolean, _
   ByVal Hidden As System.Boolean, _
   ByVal Predefined As System.Boolean, _
   ByVal Validate As System.Boolean, _
   ByVal LockInBlock As System.Boolean, _
   ByVal PositionBelowLastDefinition As System.Boolean, _
   ByVal Multilines As System.Boolean _
) As AttributeDefinition
```

### C#

```csharp
AttributeDefinition InsertAttributeDefinition2(
   System.string Name,
   System.string Caption,
   System.string DefaultValue,
   System.double PositionX,
   System.double PositionY,
   System.double PositionZ,
   System.string TextStyle,
   dsTextJustification_e Justification,
   System.double Height,
   System.double Rotation,
   System.bool Fixed,
   System.bool Hidden,
   System.bool Predefined,
   System.bool Validate,
   System.bool LockInBlock,
   System.bool PositionBelowLastDefinition,
   System.bool Multilines
)
```

### JScript

```
function InsertAttributeDefinition2(
   Name : System.String,
   Caption : System.String,
   DefaultValue : System.String,
   PositionX : System.double,
   PositionY : System.double,
   PositionZ : System.double,
   TextStyle : System.String,
   Justification : dsTextJustification_e,
   Height : System.double,
   Rotation : System.double,
   Fixed : System.boolean,
   Hidden : System.boolean,
   Predefined : System.boolean,
   Validate : System.boolean,
   LockInBlock : System.boolean,
   PositionBelowLastDefinition : System.boolean,
   Multilines : System.boolean
) : AttributeDefinition;
```

### Managed Extensions for C++

```
AttributeDefinition* InsertAttributeDefinition2(
   System.string* Name,
   System.string* Caption,
   System.string* DefaultValue,
   System.double PositionX,
   System.double PositionY,
   System.double PositionZ,
   System.string* TextStyle,
   dsTextJustification_e Justification,
   System.double Height,
   System.double Rotation,
   System.bool Fixed,
   System.bool Hidden,
   System.bool Predefined,
   System.bool Validate,
   System.bool LockInBlock,
   System.bool PositionBelowLastDefinition,
   System.bool Multilines
)
```

### C++/CLI

```cpp
AttributeDefinition^ InsertAttributeDefinition2(
   System.String^ Name,
   System.String^ Caption,
   System.String^ DefaultValue,
   System.double PositionX,
   System.double PositionY,
   System.double PositionZ,
   System.String^ TextStyle,
   dsTextJustification_e Justification,
   System.double Height,
   System.double Rotation,
   System.bool Fixed,
   System.bool Hidden,
   System.bool Predefined,
   System.bool Validate,
   System.bool LockInBlock,
   System.bool PositionBelowLastDefinition,
   System.bool Multilines
)
```

### Parameters

- `Name`: Name of the BlockAttribute
- `Caption`: Text that displays at the command window during Block insertion
- `DefaultValue`: Visible component of the BlockAttribute
- `PositionX`: x coordinate for the insertion point of the BlockAttribute
- `PositionY`: y coordinate for the insertion point of the BlockAttribute
- `PositionZ`: z coordinate for the insertion point of the BlockAttribute
- `TextStyle`: Text style of the BlockAttribute
- `Justification`: Position and alignment of the BlockAttribute text in relation to the insertion point
- `Height`: Text size of the BlockAttribute
- `Rotation`: Insertion angle of the BlockAttribute
- `Fixed`: True to make the default value of the BlockAttribute a constant value, false to make it a variable value
- `Hidden`: True to hide the BlockAttribute in Block references, false to show it
- `Predefined`: True to use the default values, false to request a value
- `Validate`: True to prompt the user for verification that the BlockAttribute value is correct when inserting a Block, false to not
- `LockInBlock`: True to lock the BlockAttribute within the Block reference, false to not
- `PositionBelowLastDefinition`: True to align the current BlockAttribute below the previous one, false to not (see **Remarks**)
- `Multilines`: True if the BlockAttribute is multiline, false if single line (see **Remarks**)

### Return Value

[IAttributeDefinition](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition.html)

## Remarks

The difference between this method and the now obsolete ISketchManager::InsertAttributeDefinition is that this method's Multilines parameter allows you to create a multiline BlockAttribute. You cannot change a BlockAttribute from single line to multiline, or vice versa, after creation.

The PositionBelowLastDefinition parameter is ignored when the entity is created in temporary mode.

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)

## Availability

DraftSight 2018 SP0
