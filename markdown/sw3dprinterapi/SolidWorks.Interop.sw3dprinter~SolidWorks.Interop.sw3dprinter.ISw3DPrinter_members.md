---
title: "ISw3DPrinter Interface Members"
project: "SOLIDWORKS 3D Printer API Help"
interface: "ISw3DPrinter_members"
member: ""
kind: "members"
source: "sw3dprinterapi/SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter_members.html"
---

# ISw3DPrinter Interface Members

The following tables list the members exposed by [ISw3DPrinter](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter.html).

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | GetAvailableMaterials | Gets an array of strings that contain available material names, such as plastic, composite, etc., that the device can use. |
| Method | GetBuildEnvelope | Gets the dimensions of the printer envelope. |
| Method | GetBuildOrientation | Gets the selected build orientation. |
| Method | GetCalculatedBoundingVolume | Gets the dimension of the calculated bounding volume in document units. |
| Method | GetCalculatedBuildTime | Gets the estimated time in minutes to build the current document. |
| Method | GetCalculatedCost | Gets the calculated cost in vendor-defined units, e.g., dollars, euros, liters of material, etc. |
| Method | GetCalculatedSurfaceArea | Gets the calculated surface area of the current document in current document units, taking into account scale and other parameters. |
| Method | GetCalculatedVolume | Gets the calculated volume of the current document in current document units, taking into account scale and other parameters. |
| Method | GetCurrentMaterial | Gets the name of the selected material. |
| Method | GetCurrentOrientationTransform | Gets the current orientation transform. |
| Method | GetCurrentPrinterName | Gets the name of current printer. |
| Method | GetDefaultBuildOrientation | Gets the default build orientation. |
| Method | GetDefaultPrintQuality | Gets the default setting for print quality. |
| Method | GetDialogConfiguration | Gets a collection of bits that represent which controls SOLIDWORKS hides or changes in the Print dialog for a given print driver. |
| Method | GetEnvelopeOrigin | Gets the default starting location for the item to be built in the build envelope, e.g. x-min, y-min, z-min. |
| Method | GetOutputOption | Gets the currently selected output option. |
| Method | GetOutputOptions | Gets an array of strings that specify how to create the rapid prototype, e.g. "Print directly to machine", "Print to queue", "Create data file", etc. |
| Method | GetPrinterComment | Gets a general-purpose string, possibly one that the user specified during installation. |
| Method | GetPrinterImageBitmap | Gets the name of the a file of a 24-bit color . bmp of dimensions 100x100 pixels that is typically an image of the printer or a corporate logo. |
| Method | GetPrinterLocation | Gets the string that the user specified during installation to indicate where the printer is located (e.g., 2nd floor office). |
| Method | GetPrinterNames | Gets the user-specified printer names, e.g., Speedy3d_1stfloor, speed3d_2ndfloor, etc. |
| Method | GetPrinterStatus | Gets the current state of the printer. |
| Method | GetPrinterType | Gets the printer model, e.g., Speedy3D 2800. |
| Method | GetPrintQuality | Gets the current print quality setting of the printer. |
| Method | GetQuantity | Gets the number of copies to print. |
| Method | GetScale | Gets the value by which to scale the document. |
| Method | GetScaleParametersForActiveDocument | Gets the values by which the document can be scaled. The values appear in the Scale box. |
| Method | OnAdvancedSettings | Called when a user clicks the Advanced Settings button on the 3D Printer tab. |
| Method | OnCancel | Called when a user clicks the Cancel button, cancels printing the document, and closes the dialog. |
| Method | OnOk | Called when a user clicks the OK button on the dialog and sends the document to the 3D printer. |
| Method | OnStartup | Called when the user selects the vendor's printer from the Name box on the 3D Printer tab. |
| Method | OnUpdateStatistics | Called when a user clicks the Update Statistics button on the 3D Printer tab and changes the build statistics. |
| Method | SetBuildOrientation | Called when a user changes a build orientation on the Build Orientation tab. |
| Method | SetCurrentMaterial | Called when a user selects the name of a material in the Material box on the 3D Printer tab. |
| Method | SetCurrentPrinterName | Sets the name of the current printer. |
| Method | SetOrientationTransform | Called when a user changes a preset orthogonal orientation or Z rotation value on the Build Orientation tab. |
| Method | SetOutputOption | Called when a user specifies how to create the rapid prototype by making a selection in the Output box on the 3D Printer tab. |
| Method | SetPrintQuality | Called when a user selects a print quality setting on the 3D Printer tab. |
| Method | SetQuantity | Called when a user sets the number of copies to print in the Number of copies box on the 3D Printer tab. |
| Method | SetScale | Called when a user sets the value by which to scale the document in the Scale box on the 3D Printer tab. |

[Top](#topBookmark)

## See Also

[ISw3DPrinter Interface](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter.html)
[SolidWorks.Interop.sw3dprinter Namespace](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter_namespace.html)
