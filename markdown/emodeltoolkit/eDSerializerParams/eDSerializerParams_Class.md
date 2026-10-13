---
title: "eDSerializerParams Class"
project: ""
interface: "eDSerializerParams"
member: ""
kind: "class"
source: "emodeltoolkit/eDSerializerParams/eDSerializerParams_Class.htm"
---

# eDSerializerParams Class

| See Also | Example | Accessors | Availability |
| --- | --- | --- | --- |

Contains options for saving eDrawings documents to disk.

NOTE: Unicode filenames are not supported. To create a Unicode filename, first create a filename with ANSI characters and then rename it.

#### Header file code

```vb
class eDSerializerParams
{
public:

eDSerializerParams(
const ECHAR * filename,
const eDImage * previewImage //Preview image or a NULL pointer
BOOL compress,
BOOL rotateenabled,
BOOL reviewenabled,
BOOL measureenabled,
BOOL simplifiedui,
BOOL stlexportenabled,
BOOL shadingenabled,
BOOL isexploded,
eDUnitsType units, //All units are in meters; this parameter only sets the default unit for when a model is opened in the eDrawings viewer. For example, if you want to describe a model in inches, you must, in your publisher program, convert your values to meters, e.g., 1 inch = .0254 meters, and then set the this parameter to eDUnitInches. That way, inches will be the default unit type that appears when the model is measured in eDrawings. Then, the values you multiplied by .0254 to convert to meters will by multiplied back by 1/.0254 to display inches. All units are in meters.
eDDisplayType display,
eDDocumentType documenttype,
eDTransform3d viewtransform,
eDColorRGB backgroundcolor,
eDColorRGB papercolor,
eDTime expiredate,
const ECHAR * password = NULL,
eDConfiguration * activeconfiguration = NULL ); //Specifies options for saving eDrawings document to disk
eDCamera initialcamera = eDCamera() //if initialcamera is specified, viewtransform is ignored
);

};
```
