---
title: "AddParameter Method (IAttributeDef)"
project: "SOLIDWORKS API Help"
interface: "IAttributeDef"
member: "AddParameter"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef~AddParameter.html"
---

# AddParameter Method (IAttributeDef)

Adds a parameter to the attribute definition using the specified name and default value.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddParameter( _
   ByVal NameIn As System.String, _
   ByVal Type As System.Integer, _
   ByVal DefaultValue As System.Double, _
   ByVal Options As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAttributeDef
Dim NameIn As System.String
Dim Type As System.Integer
Dim DefaultValue As System.Double
Dim Options As System.Integer
Dim value As System.Boolean

value = instance.AddParameter(NameIn, Type, DefaultValue, Options)
```

### C#

```csharp
System.bool AddParameter(
   System.string NameIn,
   System.int Type,
   System.double DefaultValue,
   System.int Options
)
```

### C++/CLI

```cpp
System.bool AddParameter(
   System.String^ NameIn,
   System.int Type,
   System.double DefaultValue,
   System.int Options
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NameIn`: Name to be given to the parameter (see **Remarks**)
- `Type`: Parameter type as defined in [swParamType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swParamType_e.html)
- `DefaultValue`: Default value (see **Remarks**)
- `Options`: Not used

### Return Value

True if the parameter is added successfully, false if not

## VBA Syntax

See [AttributeDef::AddParameter](ms-its:sldworksapivb6.chm::/sldworks~AttributeDef~AddParameter.html).

## Examples

[Create Attribute (VBA)](Create_Attribute_Example_VB.htm)
[Add Attribute to Feature and Include in Library Feature (VB.NET)](Add_Attribute_to_Feature_and_Include_in_Library_Feature_Example_VBNET.htm)
[Add Attribute to Feature and Include in Library Feature (C#)](Add_Attribute_to_Feature_and_Include_in_Library_Feature_Example_CSharp.htm)
[Add Attribute to Feature and Include in Library Feature (VBA)](Add_Attribute_to_Feature_and_Include_In_Library_Feature_Example_VB.htm)
[Find Attribute (C#)](Find_Attribute_Example_CSharp.htm)
[Find Attribute (VB.NET)](Find_Attribute_Example_VBNET.htm)
[Find Attribute (VBA)](Find_Attribute_Example_VB.htm)

## Remarks

Parameters cannot be added after the attribute definition is registered.

The name of the parameter given by NameIn must be unique in the attribute definition.

For parameters of type swParamTypeDouble, the DefaultValue argument allows a default value to be placed in the attribute definition parameter. This value is assigned to the parameters of newly created attribute instances.

**NOTE:** There is no way to get or set integer parameters in attributes. Instead, use [IParameter::GetDoubleValue](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IParameter~GetDoubleValue.html) and [IParameter::SetDoubleValue2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IParameter~SetDoubleValue2.html) to get and set values for integer parameters. If you need to store a negative value, define your attribute parameter as type double. SOLIDWORKS does not allow negative integer values.

## See Also

[IAttributeDef Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef.html)
[IAttributeDef Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef_members.html)
[IAttribute::Register Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef~Register.html)
[ISldWorks::DefineAttribute Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~DefineAttribute.html)
